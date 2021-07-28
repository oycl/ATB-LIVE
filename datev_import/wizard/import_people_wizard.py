from typing import List

from odoo import models, fields, exceptions, api

from odoo.addons.journal_entry_import_utilities.lib.csv import get_csv
from .german_country_map import MAP_COUNTRY_TO_CODE


class ImportPeopleWizard(models.TransientModel):
    """Imports a csv of people.

    Creates account.account, res.partner.bank and res.partner.
    If a column doesn't exist, it's not imported.
    If an account already exists, skips the line (doesn't update).
    """

    _name = "datev_import.import_people_wizard"
    _description = "Wizard for importing datev people."

    # contains 1 or 2
    col_type = fields.Char(default="Adressattyp")

    # -- Partner/Account information
    col_account = fields.Char(default="Konto")  # Unique
    col_name_company = fields.Char(default="Name (Adressattyp Unternehmen)")
    col_name_person = fields.Char(default="Name (Adressattyp natürl. Person)")
    col_vorname_person = fields.Char(default="Vorname (Adressattyp natürl. Person)")
    col_country = fields.Char(default="Land")
    col_vat = fields.Char(default="EU-UStID")
    col_street = fields.Char(default="Straße")
    col_zip = fields.Char(default="Postleitzahl")
    col_city = fields.Char(default="Ort")
    col_phone = fields.Char(default="Telefon")
    col_email = fields.Char(default="E-Mail")
    col_website = fields.Char(default="Internet")

    # -- Bank information (if empty, skip res.partner.bank)
    col_bank = fields.Char(default="Bankbezeichnung 1")
    col_iban = fields.Char(default="IBAN-Nr. 1")

    # --
    prefixes_account_payable = fields.Char()

    file = fields.Binary()

    # -- this warning field gets set if a column does not exist
    warning = fields.Char()

    SAVE_KEY = "datev_people_import.save"
    SAVE_FIELDS = [
        "col_type",
        "col_account",
        "col_name_company",
        "col_name_person",
        "col_vorname_person",
        "col_country",
        "col_vat",
        "col_street",
        "col_zip",
        "col_city",
        "col_phone",
        "col_email",
        "col_website",
        "col_bank",
        "col_country",
        "col_iban",
    ]

    @api.onchange("file")
    def validate_file(self):
        if self.file:
            self.save_fields()
            header, lines = get_csv(self.file)
            header = self._strip_header(header)
            missing_optional = self._validate_header(header)
            if missing_optional:
                self.warning = f"Optional columns not found: {', '.join(missing_optional)}, their values will be set to null."
            else:
                self.warning = False

    @staticmethod
    def _strip_header(header):
        return [column.strip() for column in header]

    def _strip_field(self, field):
        """Removes whitespace from a field in this object."""
        value = getattr(self, field)
        new_value = value.strip() if value else ""
        setattr(self, field, new_value)

    def _strip_fields(self):
        """Removes whitespace from all fields."""
        for field in self.SAVE_FIELDS:
            self._strip_field(field)

    def _validate_header(self, header: List[str]):
        """Validates header."""
        required_columns = [
            ("Typ", self.col_type),
            ("Konto", self.col_account),
        ]

        optional_columns = [
            self.col_name_company,
            self.col_name_person,
            self.col_vorname_person,
            self.col_country,
            self.col_vat,
            self.col_street,
            self.col_zip,
            self.col_city,
            self.col_phone,
            self.col_email,
            self.col_website,
            self.col_bank,
            self.col_iban,
        ]

        missing_required = [
            column for column in required_columns if column[1] not in header
        ]
        if missing_required:
            raise exceptions.UserError(
                f"Missing columns: {[f'{m[0]}: {m[1]}' for m in missing_required]}"
            )

        missing_optional = [
            column for column in optional_columns if column not in header and column
        ]
        return missing_optional

    # ---- Import Methods ----

    def run(self):
        """Runs the wizard, importing the csv into partners, accounts and banks."""
        header, lines = get_csv(self.file)
        self._validate_header(header)
        if not self.prefixes_account_payable:
            raise exceptions.UserError(
                "Mindestens ein Präfix für Verbindlichkeitskonten muss gesetzt sein."
            )
        for line in lines:
            self._set_name(line)
            self._fix_country(line)
            self.process_line(line)

    def process_line(self, line):
        """Imports a single line."""
        if not self._account_exists(line[self.col_account]):
            account = self._create_account(line)
            partner = self._create_partner(line, account)
            self._create_partner_bank(line, partner)

    def _create_account(self, line):
        """Creates an account."""
        return self.env["account.account"].create(
            dict(
                code=line.get(self.col_account),
                name=line.get("name"),
                user_type_id=self._get_type_from_prefix(line).id,
                reconcile=True,
            )
        )

    def _create_partner_bank(self, line, partner):
        """Creates a partner bank from a line."""
        if line.get(self.col_iban):
            bank_id = None
            if line.get(self.col_bank):
                bank_id = self._create_bank(line).id

            return self.env["res.partner.bank"].create(
                dict(
                    acc_number=line.get(self.col_iban),
                    bank_id=bank_id,
                    partner_id=partner.id,
                )
            )

    def _create_bank(self, line):
        """Creates a bank from a line."""
        name = line.get(self.col_bank)
        bank = self._get_bank(name)
        if bank:
            return bank
        return self.env["res.bank"].create(dict(name=name))

    def _get_bank(self, name):
        return self.env["res.bank"].search([["name", "=", name]], limit=1)

    def _create_partner(self, line, account):
        """Creates a new partner based on line, account and bank."""
        account_key = (
            "property_account_payable_id"
            if self._is_payable_account(line)
            else "property_account_receivable_id"
        )

        return self.env["res.partner"].create(
            {
                account_key: account.id,
                "name": line.get("name"),
                "is_company": self._is_company(line),
                "country_id": self._get_country(line.get(self.col_country)).id,
                "vat": self._create_vat(line),
                "street": line.get(self.col_street),
                "zip": line.get(self.col_zip),
                "city": line.get(self.col_city),
                "phone": line.get(self.col_phone),
                "email": line.get(self.col_email),
                "website": line.get(self.col_website),
            }
        )

    def _account_exists(self, code):
        """Returns whether an account exists."""
        return self.env["account.account"].search([["code", "=", code]], limit=1)

    def _is_payable_account(self, line):
        """Returns whether account is payable based on the first of the account in the line."""
        return line.get(self.col_account)[0] in self.prefixes_account_payable.split(",")

    def _get_type_from_prefix(self, line):
        """Returns the account type, based on the first of the account in the line."""
        if self._is_payable_account(line):
            return self._get_account_type("Payable")
        else:
            return self._get_account_type("Receivable")

    def _set_name(self, line):
        """Create the name based on type."""
        if self._is_company(line):
            line["name"] = line.get(self.col_name_company) or ""
        else:
            line["name"] = " ".join(
                [
                    n
                    for n in [
                        line.get(self.col_vorname_person),
                        line.get(self.col_name_person),
                    ]
                    if n
                ]
            )

    def _fix_country(self, line):
        if line.get(self.col_country) in MAP_COUNTRY_TO_CODE:
            line[self.col_country] = MAP_COUNTRY_TO_CODE[line.get(self.col_country)]

    def _is_company(self, line):
        """Maps field in line to being company or person:

        1: person
        2: company
        """
        _type = line.get(self.col_type)
        if _type not in ["1", "2"]:
            raise exceptions.UserError(
                f"[{line.get(self.col_account)}] Typ muss entweder 1 oder 2 sein."
            )
        return line.get(self.col_type) == "2"

    def _get_account_type(self, name):
        """Returns an account type with the given name."""
        return self.env["account.account.type"].search([["name", "=", name]], limit=1)

    def _get_country(self, code):
        return self.env["res.country"].search([["code", "=", code]], limit=1)

    def _create_vat(self, line):
        """If the current vat doesn't start with country code, append it."""
        country = line.get(self.col_country)

        vat = line.get(self.col_vat)
        if vat:
            if not vat.startswith(country):
                vat = country + vat
        return vat

    def save_fields(self):
        """Saves the current fields to config"""
        values = [getattr(self, field) or "" for field in self.SAVE_FIELDS]
        save_string = ";".join(values)
        self.env["ir.config_parameter"].sudo().set_param(self.SAVE_KEY, save_string)

    def default_get(self, fields_list=None):
        """Loads the current fields from config"""
        res = super().default_get(fields_list=fields_list or [])
        save_string = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(self.SAVE_KEY, default=False)
        )
        if save_string:
            values = save_string.split(";")
            _dict = {
                self.SAVE_FIELDS[index]: value for index, value in enumerate(values)
            }
            res.update(_dict)
        return res

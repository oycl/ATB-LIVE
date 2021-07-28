import datetime
from typing import List, Dict

from cachetools import cached, Cache
from odoo import models, fields, exceptions, api

from odoo.addons.journal_entry_import_utilities.lib import unlink_attachments
from odoo.addons.journal_entry_import_utilities.lib.csv import get_csv
from odoo.addons.journal_entry_import_utilities.lib.journal import get_journal
from .import_datev_columns import *

ACCOUNT_CACHE = Cache(100)
ANALYTIC_ACCOUNT_CACHE = Cache(100)

DELIMITER = ";"


class ImportWizard(models.TransientModel):
    """Wizard for importing a datev csv."""

    _name = "datev_import.import_wizard"
    _description = "Wizard for import Datev files"

    balance_account = fields.Selection(
        selection=[["Konto", "Konto"], ["Gegenkonto (ohne BU-Schlüssel)", "Gegenkonto"]]
    )
    personenkonto = fields.Selection(
        selection=[["Konto", "Konto"], ["Gegenkonto (ohne BU-Schlüssel)", "Gegenkonto"]]
    )
    year = fields.Integer(default=datetime.datetime.now().year)
    month = fields.Integer(default=datetime.datetime.now().month)
    default_partner = fields.Many2one("res.partner")
    journal_konto_is_personen = fields.Boolean(
        "Verwende Personenkonto um Journal zu finden."
    )
    add_analytic_accounts = fields.Boolean(default=False)
    account_padding = fields.Integer(default=4)

    col_groupby = fields.Char(default=COL_GROUPBY)
    col_text = fields.Char(default=COL_TEXT)

    encoding = fields.Selection(
        [("utf-8-sig", "UTF-8"), ("latin-1", "Latin-1")], default="utf-8-sig"
    )

    files = fields.Many2many(comodel_name="ir.attachment")

    @api.onchange("month")
    def validate_month(self):
        if self.month < 1:
            self.month = 1
        elif self.month > 12:
            self.month = 12

    def run(self):
        self._check_l10n_de_reports_is_installed()
        ACCOUNT_CACHE.clear()
        ANALYTIC_ACCOUNT_CACHE.clear()

        for file in self.files:
            # Need filename to log in which file errors occured.
            # noinspection PyMethodFirstArgAssignment
            self = self.with_context(filename=file.name)
            self.balance_account = self.personenkonto
            header, lines = get_csv(file.datas, encoding=self.encoding)
            self._validate_header(header)
            for line in lines:
                self._convert_and_validate_line(line)
            grouped_lines = self._group(lines)
            for lines in grouped_lines:
                self._create_journal_entry(lines)

        unlink_attachments(self)

    def _convert_and_validate_line(self, line):
        """Converts and validates line in place."""

        # Sometimes COL_UMSATZ_2 contains Euro values, while COL_UMSATZ contains dollars.
        # We always take COL_UMSATZ_2 if it is set, since all of this is in euro.
        if line[COL_UMSATZ_2]:
            line[COL_UMSATZ] = line[COL_UMSATZ_2]

        try:
            line[COL_UMSATZ] = float(line[COL_UMSATZ].replace(",", "."))
        except ValueError as e:
            raise exceptions.UserError(str(e))

        line[COL_KONTO] = self._pad_account(line[COL_KONTO])
        line[COL_GEGENKONTO] = self._pad_account(line[COL_GEGENKONTO])

        if line[COL_SOLLHABEN] not in ["H", "S", "h", "s"]:
            raise exceptions.UserError(
                f"[{self.env.context.get('filename')}] Soll/Haben-Kennzeichen not in [H, S]"
            )

        # Raise UserError if not found
        self._get_account_from_code(line[COL_KONTO])
        self._get_account_from_code(line[COL_GEGENKONTO])

    def _pad_account(self, code):
        """E.g. (self.account_padding = 4) 123 -> 0123 or 12345 -> 12345 or 1 -> 0001"""
        return "0" * max(self.account_padding - len(code), 0) + code

    def _validate_header(self, header: List[str]):
        """Validates header."""
        missing = [column for column in COLUMNS if column not in header]
        if missing:
            raise exceptions.UserError(
                f"[{self.env.context.get('filename')}] Missing columns: {missing}"
            )

    @staticmethod
    def _apply_soll_haben(sh: str, value: float):
        """Applies soll haben to value, returning positive or negative value."""
        if sh.upper() == "S":
            return -value
        else:
            return value

    def _group(self, lines: List[Dict]) -> List[List[Dict]]:
        """Groups lines by static GROUPBY and balance account fields."""
        groups = {}
        for line in lines:
            key = (line[self.col_groupby], line[self.balance_account], line[COL_DATE])
            if key not in groups:
                groups[key] = []
            groups[key].append(line)
        return list(groups.values())

    def _create_journal_entry(self, lines: List[Dict]):
        """
        Account Journal Types
            sale	    Sales
            purchase	Purchase

            cash	    Cash
            bank	    Bank
            general	    Miscellaneous

        Account Move Types
            entry	    Journal Entry
            out_invoice	Customer Invoice
            out_refund	Customer Credit Note
            in_invoice	Vendor Bill
            in_refund	Vendor Credit Note
            out_receipt	Sales Receipt
            in_receipt	Purchase Receipt

        :param lines: List of dictionaries, mapping column names to values. Number values should be preparsed to float.
        """
        journal_id = self._get_journal(lines)
        if journal_id.type in ["bank", "cash", "general"]:
            return self._create_bank_journal_entry(lines, journal_id)
        else:
            return self._create_sales_journal_entry(lines, journal_id)

    def _create_bank_journal_entry(self, lines: List[Dict], journal_id):
        """Creates journal entry for bank, cash, general journals."""
        move_lines = []
        found_partner_id = None

        # No taxes in this journal
        # Ausgleichskonto transaction is created manually
        for line in lines:
            # main account and balance account are inverted in bank
            account_balance = self._get_account_from_code(line[self._non_balance_acc()])
            account_main = self._get_account_from_code(line[self.balance_account])
            # Add one line for ausgleichkonto and non-ausgleichskonto
            if self.add_analytic_accounts:
                analytics_id = self._get_analytics_account(line[COL_KOSTENSTELLE])
            else:
                analytics_id = None

            tax_id, amount, tax_amount = self._calculate_taxes_and_amount_from_line(
                line, account_main, "entry"
            )
            move_lines.extend(
                [
                    {
                        "name": self._build_line_name(line, is_balance=is_balance),
                        # Take the net amount for main account line, or gross for balance account line
                        self._debit_or_credit(
                            line, is_balance_account=is_balance
                        ): amount
                        if not is_balance
                        else line[COL_UMSATZ],
                        "account_id": account_id.id,
                        "analytic_account_id": analytics_id.id
                        if analytics_id
                        else None,
                        "tax_ids": tax_id.ids if not is_balance and tax_id else None,
                    }
                    for is_balance, account_id in zip(
                        [True, False], [account_balance, account_main]
                    )
                ]
            )

            # We create a separate line for taxes.
            if tax_amount and tax_id:
                move_lines.append(
                    {
                        "name": tax_id.name,
                        self._debit_or_credit(
                            line, is_balance_account=False
                        ): tax_amount,
                        "account_id": self._get_tax_account(tax_id).id,
                    }
                )

            if not found_partner_id:
                found_partner_id = self._get_partner(account_main)

        self._set_line_partner(move_lines, found_partner_id)
        return self.env["account.move"].create(
            {
                **self._build_account_move_data(lines, journal_id, found_partner_id),
                "name": journal_id.a._next(),
                "move_type": "entry",
                "line_ids": [(0, 0, line) for line in move_lines],
                "ref": lines[0][self.col_groupby],
            }
        )

    def _get_tax_account(self, tax_id):
        """Finds account for given tax."""
        repartition_lines = (
            tax_id.invoice_repartition_line_ids or tax_id.refund_repartition_line_ids
        )
        account_ids = [line.account_id for line in repartition_lines if line.account_id]
        if not repartition_lines or not account_ids:
            raise exceptions.UserError(
                f"[{self.env.context.get('filename')}] Steuer {tax_id.name} hat kein Konto."
            )
        if len(account_ids) > 1:
            raise exceptions.UserError(
                f"[{self.env.context.get('filename')}] Steuer {tax_id.name} hat mehrere mögliche Konten."
            )
        return account_ids[0]

    def _create_sales_journal_entry(self, lines: List[Dict], journal_id):
        """Creates journal entry for journals not in bank, cash, general."""
        move_lines = []
        found_partner_id = None
        move_type = self._get_move_type(lines, journal_id)
        # Taxes and ausgleichskonto are handled by odoo logic
        for line in lines:
            account_main = self._get_account_from_code(line[self._non_balance_acc()])
            if self.add_analytic_accounts:
                analytics_id = self._get_analytics_account(line[COL_KOSTENSTELLE])
            else:
                analytics_id = None

            tax_id, amount, _ = self._calculate_taxes_and_amount_from_line(
                line, account_main, move_type
            )
            move_lines.append(
                {
                    "name": self._build_line_name(line),
                    "price_unit": amount,
                    "account_id": account_main.id,
                    "tax_ids": tax_id.ids if tax_id else None,
                    "analytic_account_id": analytics_id.id if analytics_id else None,
                },
            )

        codes = {line[self.balance_account] for line in lines}
        if len(codes) > 1:
            raise exceptions.UserError(
                f"[{self.env.context.get('filename')}] Zwei oder mehr Zeilen mit demselben Belegfeld 1 haben unterschiedliche Ausgleichskonto."
            )

        balance_account = self._get_account_from_code(lines[0][self.balance_account])
        if not found_partner_id:
            found_partner_id = self._get_partner(
                balance_account, default=self.default_partner
            )

        self._set_line_partner(lines, found_partner_id)
        if journal_id.type in ["sale", "purchase"]:
            name = lines[0][self.col_groupby]
            ref = ""
        else:
            name = None
            ref = lines[0][self.col_groupby]

        journal_entry = self.env["account.move"].create(
            {
                **self._build_account_move_data(lines, journal_id, found_partner_id),
                "name": name,
                "move_type": move_type,
                "invoice_line_ids": [(0, 0, line) for line in move_lines],
                "ref": ref,
            }
        )
        if not name:
            journal_entry._set_next_sequence()

        if not journal_entry.invoice_line_ids:
            raise exceptions.UserError(
                f"[{self.env.context.get('filename')}] No invoice lines created for entry {name}. "
                f"This is likely due to all accounts [{[line['account_id'] for line in move_lines]}] "
                f"being reconcilable aka internal an internal transaction."
            )

        self._set_balance_lines_account(journal_entry, balance_account)
        self._fix_tax_rounding_errors(journal_entry, lines)
        return journal_entry

    @staticmethod
    def _fix_tax_rounding_errors(journal_entry, lines: List[Dict]):
        """Fixes rounding errors in gross sum of lines by modifying the tax line."""
        # 1. group datev lines based on tax identifier
        # 2. group odoo invoice lines based on tax identifier
        # 3. find counter line (line with debit if the other have credit, and other way around)
        # 4. group odoo tax lines
        # 5. iterate over tax lines and add difference between odoo lines and datev lines to tax_line and counter_line
        tax_identifier_to_line_ids = {}
        tax_identifier_to_datev_lines = {}

        # 1.
        for line in lines:
            tax_identifier = line[COL_TAX]
            if tax_identifier:
                if tax_identifier not in tax_identifier_to_datev_lines:
                    tax_identifier_to_datev_lines[tax_identifier] = []
                tax_identifier_to_datev_lines[tax_identifier].append(line)

        # 2.
        for line_id in journal_entry.invoice_line_ids:
            if line_id.tax_ids:
                tax_identifier = line_id.tax_ids[0].l10n_de_datev_code
                if tax_identifier:
                    if tax_identifier not in tax_identifier_to_line_ids:
                        tax_identifier_to_line_ids[tax_identifier] = []
                    tax_identifier_to_line_ids[tax_identifier].append(line_id)

        # 3.
        counter_line_id = [
            line_id
            for line_id in journal_entry.line_ids
            if line_id.account_id.reconcile
        ][0]

        # 4.
        tax_identifier_to_tax_line_ids = {}
        for tax_line_id in journal_entry.line_ids:
            if tax_line_id.tax_group_id:
                tax_identifier = tax_line_id.tax_line_id.l10n_de_datev_code
                if tax_identifier:
                    if tax_identifier not in tax_identifier_to_tax_line_ids:
                        tax_identifier_to_tax_line_ids[tax_identifier] = []
                    tax_identifier_to_tax_line_ids[tax_identifier].append(tax_line_id)

        # 5.
        # multiplication and subsequent division by 100, is to avoid floating point addition problems
        for tax_identifier, tax_line_ids in tax_identifier_to_tax_line_ids.items():
            real_gross = (
                sum(
                    round(datev_line[COL_UMSATZ] * 100)
                    for datev_line in tax_identifier_to_datev_lines[tax_identifier]
                )
                / 100
            )
            odoo_gross = abs(
                (
                    sum(
                        round((line_id.debit or line_id.credit * -1) * 100)
                        for line_id in tax_identifier_to_line_ids[tax_identifier]
                    )
                    + sum(
                        round((tax_line_id.debit or tax_line_id.credit * -1) * 100)
                        for tax_line_id in tax_line_ids
                    )
                )
                / 100
            )
            diff = real_gross - odoo_gross
            if diff:
                # Assuming not len(tax_line_ids) > 1
                tax_line_id = tax_line_ids[0]
                if tax_line_id.debit:
                    try:
                        tax_line_id.debit += diff
                    except exceptions.UserError:
                        # Ignore unbalanced entry exception (entry is balanced below)
                        pass
                    counter_line_id.credit += diff
                elif tax_line_id.credit:
                    try:
                        tax_line_id.credit -= diff
                    except exceptions.UserError:
                        # Ignore unbalanced entry exception (entry is balanced below)
                        pass
                    counter_line_id.debit -= diff

    def _calculate_taxes_and_amount_from_line(
        self, line: dict, account_id, move_type: str
    ):
        tax_id = self._get_taxes(line[COL_TAX], account_id)
        if tax_id:
            tax_percentage = self._calculate_tax_percentage(tax_id, move_type)

            amount = line[COL_UMSATZ] / (1 + tax_percentage / 100.0)
            tax_amount = line[COL_UMSATZ] - amount

            # Set the default code we found (used for fixing rounding errors later on)
            if not line[COL_TAX]:
                line[COL_TAX] = tax_id.l10n_de_datev_code
        else:
            amount = line[COL_UMSATZ]
            tax_amount = 0
        return tax_id, amount, tax_amount

    @staticmethod
    def _calculate_tax_percentage(tax_id, move_type):
        """A tax id may contain multiple lines, e.g. +100% -100% which should add up to 0."""
        if move_type in ["out_invoice", "in_invoice", "entry"]:
            perc_sum = sum(
                line.factor_percent
                for line in tax_id.invoice_repartition_line_ids
                if line.repartition_type != "base"
            )
        elif move_type in ["out_refund", "in_refund"]:
            perc_sum = sum(
                line.factor_percent
                for line in tax_id.refund_repartition_line_ids
                if line.repartition_type != "base"
            )
        else:
            perc_sum = 0
        return tax_id.amount * perc_sum / 100

    def _build_account_move_data(self, input_lines, journal_id, partner_id):
        """Uses original input lines to build common account move data. Missing: type and lines."""
        return {
            "journal_id": journal_id.id,
            "date": self._get_date(input_lines[0]),
            "invoice_date": self._get_invoice_date(input_lines[0]),
            "partner_id": partner_id.id if partner_id else None,
            "imported_from": "datev",
        }

    @staticmethod
    def _set_line_partner(lines: List[Dict], partner_id):
        """Sets the partner for all lines."""
        for line in lines:
            line["partner_id"] = partner_id.id if partner_id else None

    @staticmethod
    def _set_balance_lines_account(journal_entry, balance_account):
        """Sets the account of all lines with currently reconcilable accounts."""
        for odoo_line_id in journal_entry.line_ids:
            if odoo_line_id.account_id.reconcile:
                odoo_line_id.account_id = balance_account

    @cached(ANALYTIC_ACCOUNT_CACHE)
    def _get_analytics_account(self, cost_centre):
        if not cost_centre:
            return None

        code = cost_centre[2:]
        analytic_account_id = self.env["account.analytic.account"].search(
            [["code", "=", code]]
        )
        if not analytic_account_id:
            raise exceptions.UserError(
                f"[{self.env.context.get('filename')}] Could not find analytic account for code '{code}'"
            )
        return analytic_account_id

    def _get_journal(self, lines):
        """Returns the journal for these lines."""

        # Handle internal transaction between reconcilable accounts, put into fallback
        all_account_ids = []
        for line in lines:
            all_account_ids.extend(
                [
                    self._get_account_from_code(line[self.balance_account]),
                    self._get_account_from_code(line[self._non_balance_acc()]),
                ]
            )
        if all(account_id.reconcile or False for account_id in all_account_ids):
            return get_journal(
                self.env, account_ids=[None], model="datev_import.journal_mapping"
            )

        # Get journal based on one account
        account_ids = [
            self._get_account_from_code(
                line[self.balance_account]
                if self.journal_konto_is_personen
                else line[self._non_balance_acc()]
            )
            for line in lines
        ]

        return get_journal(
            self.env,
            account_ids=[account_id.id for account_id in account_ids],
            model="datev_import.journal_mapping",
        )

    def _get_move_type(self, lines, journal_id):
        """Get correct move type according to lines, journal_id and ausgleichskonto."""
        _sum = sum(
            [
                self._apply_soll_haben(line[COL_SOLLHABEN], line[COL_UMSATZ])
                for line in lines
            ]
        )

        haben = _sum >= 0
        konto = self.balance_account == "Konto"

        if journal_id.type == "sale":
            if haben ^ konto:
                move_type = "out_invoice"
            else:
                move_type = "out_refund"
        else:  # purchase
            if haben ^ konto:
                move_type = "in_refund"
            else:
                move_type = "in_invoice"

        return move_type

    def _get_partner(self, account_id, default=None):
        """Returns partner who has the given account id."""
        partner = self.env["res.partner"].search(
            [
                "|",
                ["property_account_payable_id", "=", account_id.id],
                ["property_account_receivable_id", "=", account_id.id],
            ],
            limit=1,
        )
        if not partner and default:
            return default
        return partner

    def _get_taxes(self, bu_schluessel: str, account):
        """Gets taxes based on bu-schluessel, use account taxes as fallback."""
        tax = self.env["account.tax"].search(
            [["l10n_de_datev_code", "=", bu_schluessel]], limit=1
        )
        if not tax:
            return account.tax_ids[0] if account.tax_ids else None
        return tax

    def _build_line_name(self, line, is_balance=False):
        """Builds line name from line."""
        if not is_balance:
            return line.get(self.col_text)
        else:
            return None

    def _get_invoice_date(self, line):
        """Gets date based on information in line and settings."""
        try:
            # We have to set the year at the same time as the month/day, to avoid errors for e.g. 2020-02-29
            date = datetime.datetime.strptime(str(self.year) + line[COL_DATE], "%Y%d%m")
        except ValueError as e:
            raise exceptions.UserError(
                f"[{self.env.context.get('filename')}] Error parsing date {line[COL_DATE]}: {str(e)}"
            )
        return date

    def _get_date(self, line):
        """Overwrites invoice date if smaller than selected month to first of month."""
        date = self._get_invoice_date(line)
        if date.month != self.month:
            date = datetime.datetime(year=self.year, month=self.month, day=1)
        return date

    @cached(ACCOUNT_CACHE)
    def _get_account_from_code(self, code):
        """Gets account from code, raising an exception if it doesn't exist."""
        account = self.env["account.account"].search([["code", "=", code]], limit=1)
        if not account:
            raise exceptions.UserError(
                f"[{self.env.context.get('filename')}] Account {code} not found."
            )
        return account

    def _non_balance_acc(self):
        """Returns the column name of non ausgleichskonto."""
        if self.balance_account == "Konto":
            return "Gegenkonto (ohne BU-Schlüssel)"
        else:
            return "Konto"

    @staticmethod
    def _debit_or_credit(line: dict, is_balance_account: bool):
        """Converts H or S to debit or credit."""
        haben = line[COL_SOLLHABEN].upper() == "H"
        if haben ^ is_balance_account:
            return "debit"
        else:
            return "credit"

    def _check_l10n_de_reports_is_installed(self):
        """Check that module is installed."""
        module = self.env["ir.module.module"].search(
            [["name", "=", "l10n_de_reports"]], limit=1
        )
        if module.state != "installed":
            raise exceptions.UserError("module 'l10n_de_reports' not installed")

    @api.model
    def show_account_to_journal_mapping(self, _):
        """Redirects to list view of account to journal mapping"""
        return {
            "type": "ir.actions.act_window",
            "name": "Account to Journal Mapping",
            "res_model": "datev_import.journal_mapping",
            "view_mode": "tree",
            "target": "current",
        }

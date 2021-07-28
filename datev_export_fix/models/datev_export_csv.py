"""
Changes the export to be fully configurable.

See source: odoo/enterprise/l10n_de_reports/models/datev_export_csv.py

OVERWRITES:
* get_zip (method calling the datev and the partner export)
* get_csv (datev export)
* _get_partner_list (partner export)
"""

import io
import logging
import time
import zipfile
from datetime import datetime

from cachetools import cached, LRUCache
from odoo import models, fields, exceptions
from odoo.tools import pycompat
from typing import Optional, List, Tuple, Set
from dataclasses import dataclass, field

MATCH_CACHE = LRUCache(maxsize=1024)
ORDER_BY_NAME_CACHE = LRUCache(maxsize=1024)
PARTNER_ACCOUNT_CACHE = LRUCache(maxsize=1024)
RECONCILE_CACHE = LRUCache(maxsize=1024)

LOGGER = logging.getLogger(__name__)


@dataclass
class PartnerData:
    partner_id: models.Model
    invoice_type: str
    direct_debit_ids: List[models.Model] = field(default_factory=list)


class DatevExportCSV(models.AbstractModel):
    _inherit = "account.general.ledger"

    def get_zip(self, options):
        """Overridden. Allows usage of new datev export structure."""

        # ---- ORIGINAL COMMENT:
        # Check ir_attachment for method _get_path
        # create a sha and replace 2 first letters by something not hexadecimal
        # Return full_path as 2nd args, use it as name for Zipfile
        # Don't need to unlink as it will be done automatically by bgarbage collector
        # of attachment cron
        # This create a zip file that we store as an ir_attachment. To prevent overwritting
        # an existing ir_attachement, we store it in a folder called ww (all others attachments
        # are inside folders that only has hexadecimal value as name)
        # This is done so that we can send the zip directly to client without putting it
        # in memory. After having created the file, we also have to call _file_delete
        # Otherwise the folder ww won't be garbage collected by the cron
        # ----
        ir_attachment = self.env["ir.attachment"]
        sha = ir_attachment._compute_checksum(str(time.time()).encode("utf-8"))
        fname, full_path = ir_attachment._get_path(False, "ww" + sha[2:])
        self._clear_all_caches()
        with zipfile.ZipFile(full_path, "w", False) as zf:
            if not bool(
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("datev_export.sub_folders_enabled")
            ):
                # ----- This creates the old datev export structure -----
                zf.writestr("EXTF_accounting_entries.csv", self.get_csv(options))
            else:
                # ----- This creates the new datev export structure -----
                for (
                    filename,
                    content_or_path,
                    is_attachment,
                ) in self.get_nested_datev_export(options):
                    if not is_attachment:
                        zf.writestr(filename, content_or_path)
                    else:
                        zf.write(content_or_path, filename)
            zf.writestr("EXTF_customer_accounts.csv", self._get_partner_list(options))
        ir_attachment._file_delete(fname)
        return open(full_path, "rb")

    def get_nested_datev_export(self, options):
        """Creates folder hierarchy. Every move gets its own folder, with pdf and csv."""
        self._setup_csv_export()

        preheader = self._build_preheader(options)
        columns = self.env["datev_export.column"].search([], order="id")
        header = [column.header for column in columns]
        base_lines = [preheader, header]

        # Calculates unique value keys once
        unique_keys = {column.value for column in columns}

        # Calculates enumerated columns once
        enumerated_column_configuration = [
            (index, column.value, column.max_length)
            for index, column in enumerate(columns)
        ]

        account_moves = self._get_all_account_moves(options)

        name_content_tuples = []  # (name, content)
        for account_move in account_moves:
            output = io.BytesIO()
            writer = pycompat.csv_writer(
                output, delimiter=";", quotechar='"', quoting=2
            )

            # Makes sure every line gets only added once - this is original odoo core logic
            move_line_set = {}

            # Reuses header lines
            lines = base_lines.copy()
            for aml in account_move.line_ids:
                array = self._build_datev_export_line(
                    aml, move_line_set, unique_keys, enumerated_column_configuration
                )
                if array:
                    lines.append(array)
            writer.writerows(lines)

            # Slashes lead to folders, need to replace them
            move_name = account_move.name.replace("/", "_")

            name_content_tuples.append(
                (f"{move_name}/{move_name}.csv", output.getvalue(), False)
            )

            # Add attachment files
            for index, attachment_id in enumerate(account_move.attachment_ids):
                file_path = attachment_id._full_path(attachment_id.store_fname)
                name_content_tuples.append(
                    (
                        f"{move_name}/{move_name}{f'_{str(index)}' if index else ''}.pdf",
                        file_path,
                        True,
                    )
                )

        return name_content_tuples

    # OVERRIDDEN
    def get_csv(self, options):
        """
        Improved original get_csv method, returning a regular csv for accounting entries.
        """

        self._setup_csv_export()

        output = io.BytesIO()
        writer = pycompat.csv_writer(output, delimiter=";", quotechar='"', quoting=2)
        preheader = self._build_preheader(options)

        columns = self.env["datev_export.column"].search([], order="id")
        header = [column.header for column in columns]
        lines = [preheader, header]

        # Calculates unique value keys once
        unique_keys = {column.value for column in columns}

        # Calculates enumerated columns once
        enumerated_column_configuration = [
            (index, column.value, column.max_length)
            for index, column in enumerate(columns)
        ]

        # Iterates over all account move lines, joining and creating lines
        account_moves = self._get_all_account_moves(options)
        for account_move in account_moves:
            move_line_set = {}
            for aml in account_move.line_ids:
                array = self._build_datev_export_line(
                    aml, move_line_set, unique_keys, enumerated_column_configuration
                )
                if array:
                    lines.append(array)

        writer.writerows(lines)
        return output.getvalue()

    def _setup_csv_export(self):
        # checks for installation of required module (dependency breaks tests)
        self._check_l10n_de_reports_is_installed()

    @staticmethod
    def _clear_all_caches():
        MATCH_CACHE.clear()
        ORDER_BY_NAME_CACHE.clear()
        PARTNER_ACCOUNT_CACHE.clear()
        RECONCILE_CACHE.clear()

    def _build_preheader(self, options):
        """Builds preheader from options."""
        date_from, date_to, fiscal_year = self._get_date_strings(options)
        datev_info = self._get_datev_client_number()
        preheader = [
            "EXTF",
            510,
            21,
            "Buchungsstapel",
            7,
            "",
            "",
            "",
            "",
            "",
            datev_info[0],
            datev_info[1],
            fiscal_year,
            self._config_account_length("general"),
            date_from,
            date_to,
            "",
            "",
            "",
            "",
            0,
            "EUR",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        return preheader

    def _build_datev_export_line(
        self,
        aml,
        move_line_set: dict,
        unique_keys: set,
        enumerated_column_configuration,
    ):
        """
        :param aml: Account move line
        :param move_line_set: Contains unique identifiers for all account_move lines, creation is skipped if already exists

        ---- For optimization ---
        :param unique_keys: List of unique column keys
        :param enumerated_column_configuration: tuples (index, column.value, column.max_length)
        """
        if aml.debit == aml.credit:
            # Ignore debit = credit = 0
            return

        # If both account and counteraccount are the same, ignore the line
        if aml.account_id == aml.move_id.l10n_de_datev_main_account_id:
            return

        # If line is a tax ignore it as datev_export_fix requires single line with gross amount
        # and deduct tax itself based on account or on the control key code
        if aml.tax_line_id:
            return

        match_values = self._get_line_match_values(aml)
        to_account_code, account_code, letter, partner_id = match_values
        amount, concat_name = self._calculate_amount(aml, match_values)

        if aml.move_id.journal_id.type in ["sale", "purchase"]:
            # In sale and purchase, we group the amount (see _calculate_amount(...))
            # If this line was already added, skip it.
            match_key = "%s-%s-%s-%s" % (
                account_code,
                to_account_code,
                amount,
                aml.partner_id,
            )
            if move_line_set.get(match_key):
                return
            else:
                move_line_set[match_key] = True

        # reference
        reference = aml.move_id.name
        if aml.move_id.journal_id.type == "purchase" and aml.move_id.ref:
            reference = aml.move_id.ref

        # on receivable/payable aml of sales/purchases
        date = ""
        if to_account_code == account_code and aml.date_maturity:
            date = aml.date

        # Unused
        # partner_vat = aml.tax_ids and aml.move_id.partner_id.vat or ""

        code_correction = ""
        if not aml.account_id.tax_ids and aml.tax_ids:
            # Take the correction code from the tax
            code_correction = aml.tax_ids[0].l10n_de_datev_code

        # for bank journal type cash or bank, we need to get the reconciled corresponding account.move.line
        # main_line is the main reconciled move line
        main_line = self._get_main_account_move_line(aml, amount)

        main_line_order = self._get_order_by_name(main_line.move_id.invoice_origin)

        # Function redefinition introduces maybe 0.05 ms of overhead
        def _get_value(key: str):
            """Gets the value from the account.move.line, based on the key."""
            if not key:
                return None
            if key == "invoice_address_country":
                return main_line.move_id.partner_id.country_id.code
            elif key == "shipping_address_country":
                if not main_line.move_id.partner_shipping_id:
                    # Take country code of an order connected to this invoice
                    if main_line_order.partner_id:
                        return main_line_order.partner_id.country_id.code
                    else:
                        return None
                return main_line.move_id.partner_shipping_id.country_id.code
            elif key == "order_number":
                return main_line_order.name
            elif key == "inv_number":
                return main_line.move_id.name
            elif key == "account_move_name":
                return aml.move_id.display_name
            elif key == "account_move_line_name":
                return concat_name
            elif key == "partner_name":
                if aml.partner_id:
                    return aml.partner_id.name
                if main_line.partner_id:
                    return main_line.partner_id.name
                if main_line_order.partner_id:
                    return main_line_order.partner_id
            elif key == "journal_name":
                return aml.journal_id.name
            elif key == "journal_id":
                return aml.journal_id.id
            elif key == "account_name":
                return aml.account_id.name
            elif key == "gross_value":
                return str(amount).replace(".", ",")
            elif key == "date_ddmm":
                return aml.move_id.date.strftime("%d%m")
            elif key == "soll_haben":
                return letter
            elif key == "currency":
                return aml.currency_id.name
            elif key == "foreign_amount":
                return str(abs(aml.price_total) or "").replace(".", ",")
            elif key == "account":
                return account_code
            elif key == "counteraccount":
                return to_account_code
            elif key == "bookingkey":
                return code_correction
            elif key == "bookingreference":
                return reference
            elif key == "paymentreference":
                return aml.move_id.payment_reference
            elif key == "date":
                return date
            elif key == "rate":
                if aml.amount_currency and amount:
                    rate = (abs(aml.price_total) / amount)
                    return str(round(rate, 3)).replace(".", ",")
                else:
                    return ""
            elif key == "cost_centre_1":
                account = self._get_cost_centre_1(aml)
                return account.code if account else ""
            elif key == "cost_centre_2":
                account = self._get_cost_centre_2(aml)
                return account.code if account else ""
            elif key == "cost_centre_1_name":
                account = self._get_cost_centre_1(aml)
                return account.name if account else ""
            elif key == "cost_centre_2_name":
                account = self._get_cost_centre_2(aml)
                return account.name if account else ""
            elif key == "refund_flag":
                if aml.move_id.type in ["out_refund", "in_refund"]:
                    return "1"
                else:
                    return "0"
            else:
                return ""

        # We call get_value only once per key, then distribute the result onto any columns that want it
        column_to_value = {}
        for unique_key in unique_keys:
            column_to_value[unique_key] = str(_get_value(unique_key) or "")

        array = ["" for _ in range(116)]
        for (index, column_value, column_length,) in enumerated_column_configuration:
            array[index] = column_to_value[column_value][:column_length]
        return array

    def _get_cost_centre_1(self, aml):
        """Analytic account or first analytic account in analytic tag.

        :param aml: account.move.line
        """
        if aml.analytic_account_id:
            return aml.analytic_account_id

        if aml.analytic_tag_ids:
            return self._get_account_from_line_analytic_tag(aml, 0)

        return None

    def _get_cost_centre_2(self, aml):
        """First analytic account in analytic tag, if analytic account is set, otherwise second.

        :param aml: account.move.line
        """
        # Use second tag if first tag is used by cost_centre_1
        tag_index = 0 if aml.analytic_account_id else 1
        return self._get_account_from_line_analytic_tag(aml, tag_index)

    @staticmethod
    def _get_account_from_line_analytic_tag(aml, index):
        """
        :param aml: account.move.line
        :param index: Index of tag to get account code from
        """
        if aml.analytic_tag_ids and len(aml.analytic_tag_ids) > index:
            distribution_ids = aml.analytic_tag_ids[index].analytic_distribution_ids
            if distribution_ids:
                return distribution_ids[0].account_id

        return None

    def _get_date_strings(self, options):
        """Get date information from options.

        :returns date_from, date_to, fiscal_year (%Y%m%d)
        """
        date_from = fields.Date.from_string(options.get("date").get("date_from"))
        date_to = fields.Date.from_string(options.get("date").get("date_to"))
        fiscal_year = self.env.company.compute_fiscalyear_dates(date_to)

        date_from = datetime.strftime(date_from, "%Y%m%d")
        date_to = datetime.strftime(date_to, "%Y%m%d")
        fiscal_year = datetime.strftime(fiscal_year.get("date_from"), "%Y%m%d")
        return date_from, date_to, fiscal_year

    def _get_all_account_moves(self, options):
        """Finds all account.move which are relevant to this export.

        :returns list of account.move
        """
        moves = self.with_context(
            self._set_context(options), print_mode=True, aml_only=True
        )._get_lines(options)

        # find all account_move
        if len(moves):
            self.env.cr.execute(
                """SELECT distinct(move_id) FROM account_move_line WHERE id IN %s""",
                (tuple(moves),),
            )
            move_ids = [l.get("move_id") for l in self.env.cr.dictfetchall()]
            moves = self.env["account.move"].browse(move_ids)

        return moves

    @staticmethod
    def _adjust_length(string, n):
        """Sets length of string to n.

        Either removes characters from the right or adds "0" to the right until length is reached.
        """
        return str(string).ljust(n, "0")[:n]

    def _get_main_account_move_line(self, aml, amount):
        """Finds main account_move_line, connected to this account move line.

        For internal account.move.lines, which show internal bank movements, finds the main account.move.line
        which shows the external move.
        :param aml: account.move.line to find the main account.move.line for
        :param amount: amount of currency moved (only relevant whether it's positive or negative)
        :return: account.move.line
        """
        main_line = aml
        if aml.journal_id.type in ["bank", "cash"]:
            apr = self._get_reconcile_by_id(aml.full_reconcile_id.id)
            if amount < 0:
                main_line = apr.debit_move_id
            else:
                main_line = apr.credit_move_id

        return main_line

    def _calculate_amount(self, aml, match_values):
        """Calculates the amount for this account.move.line.

        Lines with the same match values get grouped and their amount gets added.
        """
        # Sale journals have taxes, therefore we use price_total instead of balance.
        # Lines with identical accounts, partner and sign are grouped into one datev line.
        names = []
        if aml.move_id.journal_id.type in ["sale", "purchase"]:
            amount = 0
            for _aml in aml.move_id.line_ids:
                s_match_values = self._get_line_match_values(_aml)
                if s_match_values == match_values:
                    if _aml.amount_currency and _aml.price_total:
                        # amount_currency is set -> we need to convert foreign currency gross
                        # We don't use the odoo currency conversion, since past entries might have used
                        # different conversions then currently set up.
                        rate = _aml.amount_currency / _aml.balance
                        price_total = _aml.price_total / rate
                    elif _aml.price_total:
                        # no foreign currency
                        price_total = _aml.price_total
                    else:
                        # default to _aml.balance for edge cases where an invoice in a sales journal has no price_total set
                        price_total = _aml.balance

                    amount += price_total
                    names.append(_aml.name)
        else:
            amount = abs(aml.balance)
            names = [aml.name]

        # The amount in datev is always greater 0.
        return abs(round(amount, 2)), ", ".join([str(name) for name in names if name])

    def _config_account_length(self, name):
        """Get the configured account length."""
        return (
            int(
                self.env["ir.config_parameter"]
                .sudo()
                .get_param(f"datev_export.length_{name}_accounts")
            )
            or 36
        )

    def _check_l10n_de_reports_is_installed(self):
        """Check that module is installed."""
        if not self._is_module_installed("l10n_de_reports"):
            raise exceptions.UserError("module 'l10n_de_reports' not installed")

    def _is_module_installed(self, module: str):
        """Check that module is installed."""
        module = self.env["ir.module.module"].search([["name", "=", module]])
        return module.state == "installed"

    # ---- Cached for speed ----
    @cached(RECONCILE_CACHE)
    def _get_reconcile_by_id(self, reconcile_id):
        """Gets reconcile by full_reconcile_id."""
        return self.env["account.partial.reconcile"].search(
            [["full_reconcile_id", "=", reconcile_id]], limit=1
        )

    @cached(MATCH_CACHE, key=lambda _, aml: aml.id)
    def _get_line_match_values(self, aml):
        """
        Gets parameters a line is matched on for grouping.

        :param aml: account move line
        :return: target account code, account code, letter (s/h), partner id
        """
        # account and counterpart account
        if not aml.move_id.l10n_de_datev_main_account_id:
            aml.move_id._get_datev_account()
            if not aml.move_id.l10n_de_datev_main_account_id:
                raise exceptions.UserError(
                    f"Es konnte kein eindeutiges Ausgleichskonto für folgende Buchungszeile gefunden werden: '{aml.name or aml.id}' ({aml.move_id.name})\n")

        to_account_code = self._find_partner_account(
            aml.move_id.l10n_de_datev_main_account_id, aml.partner_id
        )
        account_code = self._find_partner_account(aml.account_id, aml.partner_id)

        letter = "s" if aml.balance > 0 else "h"
        partner_id = aml.partner_id
        return to_account_code, account_code, letter, partner_id

    @cached(ORDER_BY_NAME_CACHE)
    def _get_order_by_name(self, name: str):
        return self.env["sale.order"].search([["name", "=", name]])[:1]

    @cached(
        PARTNER_ACCOUNT_CACHE, key=lambda _, account, partner: (account.id, partner.id)
    )
    def _find_partner_account(self, account, partner):
        """Finds partner account string, based on account and partner.

        Is simplified to:
            direkte_bebuchung_personenkonten
            True: use payable/receivable
            False: use partner.l10n_de_datev_identifier or start_count + partner.id
        """
        # personal account
        if account.internal_type in ("receivable", "payable") and partner:
            # Check if we have a property as receivable/payable on the partner
            # We use the property because in datev and in germany, partner can be of 2 types
            # important partner which have a specific account number or a virtual partner
            # Which has only a number. To differentiate between the two, if a partner in Odoo
            # explicitely has a receivable/payable account set, we use that account, otherwise
            # we assume it is not an important partner and his datev virtual id will be the
            # l10n_de_datev_identifier set or the id + the start count parameter.
            account = (
                account.internal_type == "receivable"
                and partner.property_account_receivable_id
                or partner.property_account_payable_id
            )
            return self._personal_account_id(partner, account)
        # general account
        len_general_acc = self._config_account_length("general")
        return self._adjust_length(account.code, len_general_acc)

    def _personal_account_id(self, partner, account):
        direkte_bebuchung_personenkonten = self.env["ir.config_parameter"].sudo().get_param("datev_export.direkte_bebuchung_personenkonten")
        if not direkte_bebuchung_personenkonten:
            # unterschiedliche Kreditoren/Debitorenkonten
            if account.internal_type == "receivable":
                param_start = (
                    self.env["ir.config_parameter"]
                        .sudo()
                        .get_param("l10n_de.datev_start_count")
                )
            else:
                param_start = (
                    self.env["ir.config_parameter"]
                        .sudo()
                        .get_param("l10n_de.datev_payable_start_count")
                )

            start_count = (
                    param_start and param_start.isdigit() and int(param_start)
            )
            return partner.l10n_de_datev_identifier or start_count + partner.id
        else:
            len_personal_acc = self._config_account_length("personal")
            return self._adjust_length(account.code, len_personal_acc)

    # ------------------- PARTNER EXPORT ---------------------

    def _build_partner_preheader(self, options, columns, sample_line):
        """Builds the preheader from the passed options."""
        date_to = fields.Date.from_string(options.get("date").get("date_to"))
        fy = self.env.company.compute_fiscalyear_dates(date_to)
        fy = datetime.strftime(fy.get("date_from"), "%Y%m%d")
        datev_info = self._get_datev_client_number()

        # find length of account code
        account_code_length = 0
        index = [index for index, column in enumerate(columns) if column.value == "code"]
        if index and sample_line:
            sample_account_code = sample_line[index[0]]
            account_code_length = len(sample_account_code)

        return [
            "EXTF",
            510,
            16,
            "Debitoren/Kreditoren",
            4,
            None,
            None,
            "",
            "",
            "",
            datev_info[0],
            datev_info[1],
            fy,
            account_code_length,
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]

    def _get_partner_export_partners(
        self, options, direct_debit=False
    ) -> List[PartnerData]:
        """Gets list of partners with their associated direct debits."""
        move_line_ids = self.with_context(
            self._set_context(options), print_mode=True, aml_only=True
        )._get_lines(options)

        if not len(move_line_ids):
            return []

        # Gets one entry for each partner, invoice type combination
        self.env.cr.execute(
            """
            SELECT distinct(aml.partner_id, m.move_type), aml.partner_id, m.move_type
            FROM account_move_line aml
            LEFT JOIN account_move m
                ON aml.move_id = m.id
            WHERE aml.id IN %s
                AND aml.tax_line_id IS NULL
                AND aml.debit != aml.credit
                AND aml.account_id != m.l10n_de_datev_main_account_id""",
            (tuple(move_line_ids),),
        )
        result = self.env.cr.dictfetchall()

        # Creates PartnerData objects from query results
        # Groups in_invoices and out_invoices
        partner_ids = self.env["res.partner"].browse(
            [p.get("partner_id") for p in result]
        )
        invoice_types = [p.get("move_type") for p in result]

        partner_dict = {}
        for partner_id, invoice_type in zip(partner_ids, invoice_types):
            if invoice_type == "entry":
                continue

            if partner_id.id not in partner_dict:
                partner_dict[partner_id.id] = {}

            invoice_type = "out" if invoice_type.startswith("out") else "in"
            if invoice_type not in partner_dict[partner_id.id]:
                partner_dict[partner_id.id][invoice_type] = PartnerData(
                    partner_id=partner_id,
                    invoice_type=invoice_type,
                )

        # Adds direct debit information to partner objects
        if partner_dict and direct_debit:
            self.env.cr.execute(
                """
                SELECT sdd.partner_id, sdd.id
                FROM sdd_mandate sdd
                WHERE sdd.partner_id in %s
                AND sdd.state = 'active'
                """,
                (tuple(partner_ids.ids),),
            )
            result = self.env.cr.dictfetchall()
            dd_ids = self.env["sdd.mandate"].browse([p.get("id") for p in result])
            partner_ids = [p.get("partner_id") for p in result]
            for partner_id, dd in zip(partner_ids, dd_ids):
                for partner_data in partner_dict[partner_id].values():
                    partner_data.direct_debit_ids.append(dd)

        partner_values_list = [p.values() for p in partner_dict.values()]
        return [partner_data for sublist in partner_values_list for partner_data in sublist]

    def _build_partner_line(
        self,
        enumerated_column_configuration: List[Tuple[int, Optional[str], Optional[int]]],
        unique_keys: Set[str],
        partner: PartnerData,
    ):
        """
        Builds a csv line, based on the given partner and column configuration.

        These two parameters could be simplified by passing columns, we keep them separate for less computations.
        :param enumerated_column_configuration: Tuples (index, column_value aka header, length)
        :param unique_keys: Set of unique column values, aka keys

        :param partner: Partner data to create line for.
        """

        p_id = partner.partner_id

        # Function redefinition introduces maybe 0.05 ms of overhead
        def _get_value(key: str):
            """Gets the value from the partner, based on the key."""
            if not key:
                return None
            elif key == "natural":
                return "2" if p_id.is_company else "1"
            elif key == "code":
                if partner.invoice_type.startswith("out"):
                    return self._personal_account_id(p_id, p_id.property_account_receivable_id)
                else:  # "in_*" or "entry
                    return self._personal_account_id(p_id, p_id.property_account_payable_id)
            elif key == "company_name":
                return p_id.name if p_id.is_company else ""
            elif key == "person_name":
                return "" if p_id.is_company else p_id.name
            elif key.startswith("bank_"):
                if not p_id.bank_ids:
                    return ""

                num = int(key.split("bank_")[1]) - 1  # e.g. iban_1 -> 1
                if num >= len(p_id.bank_ids):
                    return ""
                bank_account = p_id.bank_ids[num]
                return bank_account.bank_id.bic if bank_account.bank_id else ""
            elif key == "email":
                return p_id.email
            elif key.startswith("iban_"):
                if not p_id.bank_ids:
                    return ""

                num = int(key.split("iban_")[1]) - 1  # e.g. iban_1 -> 1
                if num >= len(p_id.bank_ids):
                    return ""
                bank_account = p_id.bank_ids[num]
                return bank_account.acc_number if bank_account else ""
            elif key == "country":
                return p_id.country_id.code
            elif key.startswith("dd_end_date"):
                dd = self._get_partner_dd_from_key_suffix(partner, key)
                if not dd:
                    return None
                return dd.end_date
            elif key.startswith("dd_iban"):
                dd = self._get_partner_dd_from_key_suffix(partner, key)
                if not dd:
                    return None
                return dd.partner_bank_id.acc_number
            elif key.startswith("dd_identifier"):
                dd = self._get_partner_dd_from_key_suffix(partner, key)
                if not dd:
                    return None
                return dd.name
            elif key.startswith("dd_start_date"):
                dd = self._get_partner_dd_from_key_suffix(partner, key)
                if not dd:
                    return None
                return dd.start_date
            elif key == "lastname_person":
                if p_id.is_company:
                    return ""
                split_name = p_id.name.split(" ")
                return split_name[1] if len(split_name) > 1 else p_id.name
            elif key == "city":
                return p_id.city
            elif key == "zip":
                return p_id.zip
            elif key == "vat":
                return p_id.vat
            elif key == "street":
                return p_id.street
            elif key == "phone":
                return p_id.phone
            elif key == "firstname_person":
                if p_id.is_company:
                    return ""
                split_name = p_id.name.split(" ")
                return split_name[0] if len(split_name) > 1 else ""
            elif key == "website":
                return p_id.website
            else:
                return ""

        # We call get_value only once per key, then distribute the result onto any columns that want it
        column_to_value = {}
        for unique_key in unique_keys:
            column_to_value[unique_key] = str(_get_value(unique_key) or "")

        array = ["" for _ in range(243)]
        for (index, column_value, column_length,) in enumerated_column_configuration:
            array[index] = column_to_value[column_value][:column_length]
        return array

    @staticmethod
    def _get_partner_dd_from_key_suffix(partner, key):
        """
        If key ends with _1, we return the first direct debit for the partner.
        """
        if not partner.direct_debit_ids:
            return None

        num = int(key.split("_")[-1]) - 1  # e.g. iban_1 -> 1
        if num >= len(partner.direct_debit_ids):
            return None
        return partner.direct_debit_ids[num]

    def _get_partner_list(self, options):
        """Creates csv containing partner information.

        OVERWRITES EXISTING METHOD.
        """
        output = io.BytesIO()
        writer = pycompat.csv_writer(output, delimiter=";", quotechar='"', quoting=2)

        columns = self.env["datev_export.partner_column"].search([])

        # Calculates unique value keys once
        unique_keys = {column.value for column in columns}
        direct_debit_information_included = any(
            (key or "").startswith("dd_") for key in unique_keys
        ) and self._is_module_installed("account_sepa_direct_debit")

        # Calculates enumerated columns once
        enumerated_column_configuration = [
            (index, column.value, column.max_length)
            for index, column in enumerate(columns)
        ]

        header = [column.header or "" for column in columns]
        lines = []

        partners = self._get_partner_export_partners(
            options, direct_debit_information_included
        )
        for partner_id in partners:
            lines.append(
                self._build_partner_line(
                    enumerated_column_configuration, unique_keys, partner_id
                )
            )

        preheader = self._build_partner_preheader(options, columns, lines[0] if lines else None)
        lines = [preheader, header, *lines]
        writer.writerows(lines)
        return output.getvalue()

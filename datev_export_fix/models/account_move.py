from odoo import models, api


class AccountMoveL10NDe(models.Model):
    _inherit = "account.move"

    @api.depends(
        "journal_id",
        "line_ids",
        "journal_id.default_account_id",
    )
    def _get_datev_account(self):
        """Extends get datev account method to account for clearing accounts (Verrechnungskonto).
        A clearing account is usually a temporary account containing costs or
        amounts that are to be transferred to another account.

        Example:

        S   [AAAA]    100     [XXXX Lohnverbindlichkeiten]
        S   [AAAA]    100     [XXXX Lohnverbindlichkeiten]
        H   [AAAA]    180     [YYYY Auszahlung]
        H   [AAAA]    20      [ZZZZ Steuer]

        which is equivalent to this in Odoo:

        Account                         S       H
        ---------------------------------------------
        [XXXX Lohnverbindlichkeiten]    0       100
        [XXXX Lohnverbindlichkeiten]    0       100
        [AAAA]                          100     0
        [AAAA]                          100     0
        [AAAA]                          0       180
        [AAAA]                          0       20
        [YYYY Auszahlung]               180     0
        [ZZZZ Steuer]                   20      0

        which should result in [AAAA] being selected as account.

        This results in the following conditions for an account.
        1. total credit = total debit for the lines with the account
        2. The debit of the lines with the account make up half of the total debit.
        2. The credit of the lines with the account make up half of the total credit.
        """
        super()._get_datev_account()
        for move in self:
            if not move.l10n_de_datev_main_account_id:
                # Maps account_id to the lines with the given account
                account_to_lines = {}
                for aml in move.line_ids:
                    if aml.account_id not in account_to_lines:
                        account_to_lines[aml.account_id] = []
                    account_to_lines[aml.account_id].append(aml)

                # Check conditions for each account
                total_debit = sum(aml.debit for aml in move.line_ids)
                total_credit = sum(aml.credit for aml in move.line_ids)
                for account_id, amls in account_to_lines.items():
                    condition_1 = sum([aml.balance for aml in amls]) == 0
                    condition_2 = sum([aml.debit for aml in amls]) == total_debit / 2
                    condition_3 = sum([aml.credit for aml in amls]) == total_credit / 2

                    if condition_1 and condition_2 and condition_3:
                        move.l10n_de_datev_main_account_id = account_id
                        break

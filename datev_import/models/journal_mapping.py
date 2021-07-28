from odoo import models, fields


class DatevJournalMapping(models.Model):
    """Maps accounts to journals. Mapping is prioritized by sequence number."""

    _name = "datev_import.journal_mapping"
    _description = "Account to Journal Mapping"
    _order = "sequence"

    account_id = fields.Many2one("account.account")
    journal_id = fields.Many2one("account.journal")
    sequence = fields.Integer(default=0)

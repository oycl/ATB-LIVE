from odoo import api, models, fields


class AccountMove(models.Model):
    """Extends journal entries:"""

    _inherit = "account.move"

    # Where this journal entry was imported from.
    imported_from = fields.Char()

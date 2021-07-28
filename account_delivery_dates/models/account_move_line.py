from odoo import models, fields, api, _
from .account_move import AccountMove


class JournalEntryLine(models.Model):
    _inherit = "account.move.line"

    delivery_start_date = fields.Date(
        "Delivery Start date", default=lambda self: self.move_id.delivery_start_date
    )
    delivery_end_date = fields.Date(
        "Delivery End date", default=lambda self: self.move_id.delivery_end_date
    )

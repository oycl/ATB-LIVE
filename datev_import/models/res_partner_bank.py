from odoo import models


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    # Remove account_number constraint
    _sql_constraints = [
        ("unique_number", "Check(1=1)", "Account Number must be unique"),
    ]

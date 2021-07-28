from odoo import models, fields


class ExtendedBaseDocumentLayout(models.TransientModel):
    """
    Class extending base.document.layout with the necessary company fields for customized layouts
    """

    _inherit = "base.document.layout"

    street = fields.Char(related="company_id.street", readonly=True)
    street2 = fields.Char(related="company_id.street2", readonly=True)
    zip = fields.Char(related="company_id.zip", readonly=True)
    city = fields.Char(related="company_id.city", readonly=True)
    company_registry = fields.Char(related="company_id.company_registry", readonly=True)
    managing_partner = fields.Char(related="company_id.managing_partner", readonly=True)

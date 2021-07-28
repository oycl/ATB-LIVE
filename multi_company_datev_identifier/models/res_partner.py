from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    l10n_de_datev_identifier = fields.Integer(
        string="Datev Identifier",
        copy=False,
        tracking=True,
        help="The Datev identifier is a unique identifier for exchange with the government. "
        "If you had previous exports with another identifier, you can put it here. "
        "If it is 0, then it will take the database id + the value in the system parameter "
        "l10n_de.datev_start_count. ",

        # --------------- Changes here add multi company
        company_dependent=True
    )

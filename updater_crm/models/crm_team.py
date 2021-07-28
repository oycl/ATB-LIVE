# -*- coding: utf-8 -*-

from odoo import models, fields, _


class SalesTeam(models.Model):
    _inherit = "crm.team"

    report_text = fields.Char(
        string=_("Report Text"),
        help=_("Sale/Invoice text that will be displayed in the reports."),
        default=False,
    )

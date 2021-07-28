# -*- coding: utf-8 -*-

from odoo import models, fields


class Settings(models.Model):
    _inherit = "res.company"

    managing_partner = fields.Char(string="Managing Partner", default=False)

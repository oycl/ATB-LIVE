# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"
    delivery_start_date = fields.Date("Delivery Start date")
    delivery_end_date = fields.Date("Delivery End date")

    def _prepare_invoice(self):
        invoice_data = super()._prepare_invoice()
        invoice_data["delivery_start_date"] = self.delivery_start_date
        invoice_data["delivery_end_date"] = self.delivery_end_date
        return invoice_data

# -*- coding: utf-8 -*-
{
    "name": "much. | Updater Accounting",
    "summary": """
        Automatically update and set QWeb reports (Accounting)""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Technical",
    "version": "14.0.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "account", "updater"],
    # always loaded
    "data": [
        "data/account/report_invoice.xml",
        "data/account/report_invoice_document.xml",
        "data/account/report_invoice_with_payments.xml",
        "data/account/report_invoice_document_bw.xml",
        "data/account/report_invoice_document_colorful.xml",
        "data/account/report_invoice_document_slick.xml",
        "data/account/report_invoice_document_with_payments_bw.xml",
        "data/account/report_invoice_document_with_payments_colorful.xml",
        "data/account/report_invoice_document_with_payments_slick.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "auto_install": True,
    "active": True,
}

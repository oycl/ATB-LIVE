# -*- coding: utf-8 -*-
{
    "name": "much. | Updater CRM",
    "summary": """
        Enhancement for CRM with Updater Reports
    """,
    "description": """
        - Adds report_text field to CRM. Field will be printed on Sale/Invoice.
    """,
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Technical",
    "version": "14.0.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "crm", "updater", "updater_account"],
    # always loaded
    "data": [
        "views/crm_team.xml",
        "data/account/report_invoice_document.xml",
        "data/account/report_invoice_document_bw.xml",
        "data/account/report_invoice_document_colorful.xml",
        "data/account/report_invoice_document_slick.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "auto_install": True,
    "active": True,
}

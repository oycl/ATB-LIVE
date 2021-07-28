# -*- coding: utf-8 -*-
{
    "name": "much. | Updater Sale",
    "summary": """
        Automatically update and set QWeb reports (Sales)""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Technical",
    "version": "14.0.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale_management", "updater"],
    # always loaded
    "data": [
        "data/sale/report_saleorder.xml",
        "data/sale/report_saleorder_document.xml",
        "data/sale/report_saleorder_document_bw.xml",
        "data/sale/report_saleorder_document_colorful.xml",
        "data/sale/report_saleorder_document_slick.xml",
        "data/sale/report_saleorder_document_optional.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "auto_install": True,
    "active": True,
}

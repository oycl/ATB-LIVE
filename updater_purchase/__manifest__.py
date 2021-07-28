# -*- coding: utf-8 -*-
{
    "name": "much. | Updater Purchase",
    "summary": """
        Automatically update and set QWeb reports (Purchase)""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Technical",
    "version": "14.0.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "purchase", "updater"],
    # always loaded
    "data": [
        "data/purchase/report_purchaseorder.xml",
        "data/purchase/report_purchaseorder_document.xml",
        "data/purchase/report_purchaseorder_document_bw.xml",
        "data/purchase/report_purchaseorder_document_colorful.xml",
        "data/purchase/report_purchaseorder_document_slick.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "auto_install": True,
    "active": True,
}

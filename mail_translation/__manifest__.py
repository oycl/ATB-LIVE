# -*- coding: utf-8 -*-
{
    "name": "Mail German Translations",
    "summary": """""",
    "description": """Mail module translations""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "14.0.1.0",
    # any module necessary for this one to work correctly
    "depends": ["much_german_translation", "mail"],
    # always loaded
    "data": ["security/ir.model.access.csv",],
    # only loaded in demonstration mode
    "demo": [],
    "auto_install": True,
    "active": True,
}
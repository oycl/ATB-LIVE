# -*- coding: utf-8 -*-
{
    "name": "Odoo für Deutschland Installer",
    "summary": """""",
    "description": """Automatically install all OfD modules.""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "14.0.1.0",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "updater",
        "account_delivery_dates",
        "datev_export_fix",
        "much_german_translation",
    ],
    # always loaded
    "data": [],
    # only loaded in demonstration mode
    "demo": [],
    "application": True,
}

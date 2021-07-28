# -*- coding: utf-8 -*-
{
    "name": "much. QWeb Updater",
    "summary": """Automatically update and set QWeb templates""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Technical Settings",
    "version": "14.0.2.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "web"],
    # external python (pip) dependencies
    # TODO: Add external dependencies when possible to dynamically generate the ci/design of Odoo
    # "external_dependencies": {"python": ["libsass", "chevron"]},
    # always loaded
    "data": [
        # TODO: related to dynamic ci/design of Odoo
        # "views/ir_settings.xml",
        "security/ir.model.access.csv",
        "views/res_company.xml",
        "data/web/external_layout_standard_bw.xml",
        "data/web/external_layout_standard_colorful.xml",
        "data/web/external_layout_standard_slick.xml",
        "data/web/external_layout_standard.xml",
        "data/paperformat/base_paperformat_data.xml",
        "data/report_layout/report_layout_custom.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "application": True,
}

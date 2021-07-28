# -*- coding: utf-8 -*-
{
    "name": "datevexportfix",
    "summary": "Better Datev Export",
    "description": """
    Changes the datev export to be fully configurable.
    
    After installing, go to Settings > Datev Export to set up your custom configuration.
    The default custom configuration corresponds to original odoo behaviour.
    """,
    "author": "much.",
    "auto_install": False,
    "application": False,
    "version": "0.0.1",
    "sequence": 2,
    "depends": ["sale", "l10n_de_reports"],
    "data": [
        "views/config_views.xml",
        "security/ir.model.access.csv",
        "data/default.xml",
        "data/default_partner.xml",
        "data/parameter.xml",
    ],
}

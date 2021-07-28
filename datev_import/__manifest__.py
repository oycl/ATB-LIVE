# -*- coding: utf-8 -*-
{
    "name": "Datev Import",
    "summary": "Datev Import",
    "description": """
    Allows to import Datev files (as .csv), creating the correct journal entries in the appropriate journal.
    Wizard can be found under Accounting > Accounting > Actions > Datev Import.
    """,
    "category": "Invoicing",
    "author": "much.",
    "auto_install": False,
    "application": False,
    "version": "0.0.1",
    "sequence": 2,
    "depends": ["journal_entry_import_utilities"],
    "data": [
        "security/ir.model.access.csv",
        "views/import_datev_wizard.xml",
        "views/import_people_wizard.xml",
        "views/journal_mapping.xml",
        "views/reconcile_datev.xml",
    ],
}

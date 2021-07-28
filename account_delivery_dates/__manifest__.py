# -*- coding: utf-8 -*-
{
    "name": "Invoice delivery timeframe",
    "summary": "Add delivery time frame to invoice model",
    "description": """
    - New(Account) : Extend accounting model and add delivery start and end date to odoo invoice.                           
    """,
    "author": "much. GmbH",
    "auto_install": False,
    "application": False,
    "version": "14.0.1",
    "sequence": 1,
    # any module necessary for this one to work correctly
    "depends": ["base", "account", "sale_management"],
    # always loaded
    "data": [
        "views/account_move.xml",
        "views/sale_order.xml",
        "views/account_move_line.xml",
    ],
}

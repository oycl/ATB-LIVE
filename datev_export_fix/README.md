# datev_export_fix

Improves the datev export. 
Go to **Accounting > Reporting > General Ledger > EXPORT DATEV (ZIP)** 
to see the export button. Go to **Settings > Datev Export** to see the settings.



## Improvements

* Set the length of exported account numbers
* Configure column names and content
* Improvements to how certain fields are exported
* Optionally export to per-invoice subfolders with separate csvs


## Architecture

The core functions that are overridden are:
* `get_zip`
* `get_csv`

in `account.general.ledger`. These are overwritten in **models/datev_export_csv.py**.

Unfortunately, there was no way of granularily insert improvements, and I had 
to overwrite everything by copypasting the existing export. 
Just assume all the ugly code to be code from odoo (e.g. the matching logic).

Most settings are stored as `ir.config_parameter`. 
Additionally, there are two new models that store the column configurations:
* `datev_export.column`
* `datev_export.partner_column`

These inherit from `datev_export.abstract_column`, which provides common utility functions.

### get_zip(...)
`get_zip` originally called `get_csv`. It was changed to optionally call
`get_nested_datev_export()` which is a different type of export.

### get_csv(...)
`get_csv` returns a big csv string containing all datev lines. It finds a list of 
`account.move`s to export and then calls `_build_datev_export_line` to create datev
lines from them. See the code for a detailed description.

### get_nested_datev_export(...)
`get_nested_datev_export` also calls `_build_datev_export_line`, but creates multiple
files and directories.

## Account numbers
Based on the settings account numbers are calculated differently (see `_find_partner_account(...)`.
The following values are relevant:

* **direkte_bebuchung_personenkonten** (bool): ir.config_parameter (= direct_booking_person_accounts enabled)
* **l10n_de.datev_start_count** (int): ir.config_parameter
* **l10n_de.datev_payable_start_count** (int): ir.config_parameter
* **account.internal_type == "receivable"** (bool)
* **account.id** (int)
* **account.code** (str)
* **l10n_de_datev_identifier**

|                       | **direct booking**    | **l10n_de_datev_identifier set (no direct booking)** | **l10n_de_datev_identifier not set (no direct booking)**   |
| ---                   | ---       | ---       | --- |
| **receivable**        |   account.code   |  account.l10n_de_datev_identifier     | l10n_de.datev_start_count + account.id |
| **payable**           |   account.code   |  account.l10n_de_datev_identifier     | l10n_de.datev_payable_start_count + account.id | 

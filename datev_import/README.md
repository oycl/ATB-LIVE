# datev_import

Adds two wizards and one button for the import of datev files into odoo and their reconciliation.
Go to **Accounting > Accounting > Import Datev** and 
**Accounting > Accounting > Import Datev Accounts** to access the import wizards and reconciliation button.

## Import Datev
_Imports a EXTF_accounting_entries.csv file._

| Field | Technical | Description |
| --- | --- | --- |
| Personenkonto | `personenkonto` |Which of the two column options is the one containing personal accounts. |
| Jahr | `year` | Year to import (since DATEV doesn't know years) |
| Monat | `month` | Month to import, overwrites dates to have this month if prior to it. |
| Default Partner | `default_partner` | If no partner is found for an entry, this partner is used. |
| Gruppierung | `col_groupby` | Lines are grouped into entries based on values in this column name. |
| Zeilenbeschriftung | `col_text` | Column to use for line names |
| Personenkonto für Journal nutzen | `journal_konto_is_personen` | Whether to use the account defined as _'Personenkonto'_ to find the journal or the other account. |
| Analytic Accounts hinzufügen | `add_analytic_accounts` | Whether to use the value in _"KOST1 - Kostenstelle"_ to add analytic accounts to lines. |
| Kontolänge | `account_padding` | Which length to pad accounts to, e.g. if 4: `123 -> 0123` or `12345 -> 12345` or `1 -> 0001`.
| Encoding | `encoding` | How the file to import is encoded |
| -> Edit Account to Journal Mapping | `datev_import.journal_mapping` | Maps accounts to journals, used for journal selection, see also _"Personenkonto für Journal nutzen"_ |
| Files | `files` | Files to import |

## Import Datev Accounts
_Imports a EXTF_customer_accounts.csv file._

| Field | Technical | Description |
| --- | --- | --- |
| Spaltennamen Kontakt | ... | Column names to extract the corresponding value in `res.partner` from. |
| Spaltennamen Kontoinformation | ... | Column names to extract values for `account.bank` from. |
| Präfixe für Kreditorenkonten | `prefixes_account_payable` | If an account starts with one of these comma separated values, it's regarded as payable account. |

## Reconcile Datev
_Just a button, no settings. Reconciles entries imported via the above importers._


## Technical
Both wizards inherit from `SaveableWizard` which allows them to save their values, so the user does not have
to reenter everything everytime. They also use the utilities provided in `journal_entry_import_utilities`.
Also, since countries names are in German, they are mapped to their codes using the hardcoded mapping in `german_country_map.py`.
If there are ever major changes to the world map, please remember to update them here.





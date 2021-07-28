# journal_entry_import_utilities

Provides utility functions:

* `get_journal(...)`:  Uses the account to journal mapping to find the correct journal for the given account.
* `get_csv(...)`: Converts a binary csv file to a header and its lines.


Also adds a field to `account.move`:

* `imported_from` (Char): use this field when importing to denote the source

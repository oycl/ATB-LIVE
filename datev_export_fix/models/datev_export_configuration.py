from odoo import models, fields


class DatevExportColumn(models.Model):
    """Contains configuration for one column in the datev export."""

    _name = "datev_export.column"
    _description = "Datev export column"
    _inherit = "datev_export.abstract_column"

    value = fields.Selection(
        selection=[
            ("order_number", "Auftragsnummer"),
            ("gross_value", "Bruttowert"),
            ("bookingreference", "Buchungssatzreferenz"),
            ("paymentreference", "Zahlungsreferenz"),
            ("bookingkey", "Buchungsschlüssel"),
            ("date", "Datum"),
            ("date_ddmm", "Datum (DDMM)"),
            ("counteraccount", "Gegenkonto"),
            ("journal_id", "Journal ID"),
            ("journal_name", "Journalname"),
            ("account", "Konto"),
            ("account_name", "Kontoname"),
            ("rate", "Kurs"),
            ("shipping_address_country", "Lieferadresse (Land)"),
            ("partner_name", "Partnername"),
            ("invoice_address_country", "Rechnungsaddresse (Land)"),
            ("account_move_name", "Rechnungsname"),
            ("inv_number", "Rechnungsnummer"),
            ("account_move_line_name", "Rechnungszeilenname"),
            ("soll_haben", "Soll/Haben Kennzeichen"),
            ("currency", "Währung"),
            ("foreign_amount", "Bruttowert in Fremdwährung"),
            ("cost_centre_1", "Kostenstelle 1 (Code)"),
            ("cost_centre_2", "Kostenstelle 2 (Code)"),
            ("cost_centre_1_name", "Kostenstelle 1 (Name)"),
            ("cost_centre_2_name", "Kostenstelle 2 (Name)"),
            ("refund_flag", "Generalumkehr"),
        ]
    )

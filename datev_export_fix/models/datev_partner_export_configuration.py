from odoo import models, fields


class DatevExportColumn(models.Model):
    """Contains the configuration for one column in the datev partner export."""

    _name = "datev_export.partner_column"
    _description = "Datev partner export column"
    _inherit = "datev_export.abstract_column"

    value = fields.Selection(
        selection=[
            # ---- These four columns are the one defined in odoo core
            ("natural", "Addressatentyp"),
            ("code", "Konto"),
            ("company_name", "Name (Firma)"),
            ("person_name", "Name (Person)"),
            # ---- We add these columns
            ("email", "Email"),
            ("country", "Land"),
            ("lastname_person", "Nachname"),
            ("city", "Ort"),
            ("zip", "PLZ"),
            ("vat", "SteuerID"),
            ("street", "Straße"),
            ("phone", "Telefon"),
            ("firstname_person", "Vorname"),
            ("website", "Website"),
            *[
                value for subarray in
                [
                    [
                        (f"iban_{index}", f"IBAN {index}"),
                        (f"bank_{index}", f"BIC {index}"),
                        (f"dd_iban_{index}", f"Lastschrift IBAN {index}"),
                        (f"dd_identifier_{index}", f"Lastschrift ID {index}"),
                        (f"dd_start_date_{index}", f"Lastschrift Startdatum {index}"),
                        (f"dd_end_date_{index}", f"Lastschrift Enddatum {index}"),
                    ]
                    for index in range(1, 11)
                ]
                for value in subarray
            ]
        ]
    )

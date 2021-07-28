from odoo import models, fields, api


class DatevExportSettings(models.TransientModel):
    """Contains settings for datev export.

    Settings:
    * length personal accounts [int]: personal account strings get extended or cut to this length
    * length general accounts [int]: general account strings get extended or cut to this length
    * sub folders enabled: bool: enables sub folder logic, where each entry gets its own folder with document

    * link to: Entry export columns
    * link to: Partner export columns
    These control the structure of the datev export.
    """

    _inherit = "res.config.settings"

    length_personal_accounts = fields.Integer()
    length_general_accounts = fields.Integer()
    sub_folders_enabled = fields.Boolean(default=False)
    direkte_bebuchung_personenkonten = fields.Boolean(default=False)
    payable_format = fields.Integer(default=700000000)
    receivable_format = fields.Integer(default=100000000)

    @api.model
    def set_values(self):
        super(DatevExportSettings, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "datev_export.length_personal_accounts", self.length_personal_accounts
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "datev_export.length_general_accounts", self.length_general_accounts
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "datev_export.sub_folders_enabled", self.sub_folders_enabled
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "datev_export.direkte_bebuchung_personenkonten", self.direkte_bebuchung_personenkonten
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "l10n_de.datev_payable_start_count", self.payable_format
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "l10n_de.datev_start_count", self.receivable_format
        )

    @api.model
    def get_values(self):
        res = super(DatevExportSettings, self).get_values()
        lpa = int(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("datev_export.length_personal_accounts")
        )
        lga = int(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("datev_export.length_general_accounts")
        )
        sub = bool(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("datev_export.sub_folders_enabled")
        )
        dbp = bool(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("datev_export.direkte_bebuchung_personenkonten")
        )
        recfor = int(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("l10n_de.datev_start_count")
        )
        payfor = int(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("l10n_de.datev_payable_start_count")
        )

        res.update(
            length_personal_accounts=lpa,
            length_general_accounts=lga,
            sub_folders_enabled=sub,
            direkte_bebuchung_personenkonten=dbp,
            payable_format=payfor or 100000000,
            receivable_format=recfor or 700000000,
        )
        return res

    @api.model
    def show_datev_export_columns_list(self, context=None):
        """Show tree view of columns. Used in general settings."""
        return {
            "type": "ir.actions.act_window",
            "name": "Datev Export Columns",
            "res_model": "datev_export.column",
            "view_mode": "tree,form",
            "target": "current",
        }

    @api.model
    def show_datev_partner_export_columns_list(self, context=None):
        """Show tree view of columns. Used in general settings."""
        return {
            "type": "ir.actions.act_window",
            "name": "Datev Partner Export Columns",
            "res_model": "datev_export.partner_column",
            "view_mode": "tree,form",
            "target": "current",
        }

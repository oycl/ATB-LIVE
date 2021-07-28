"""Inherit this to save fields and load them as default."""


class SaveableWizard:
    SAVE_FIELDS = []
    SAVE_KEY = ""

    def save_fields(self):
        """Saves the current fields to config"""
        values = [getattr(self, field) or "" for field in self.SAVE_FIELDS]
        save_string = ";".join(values)
        self.env["ir.config_parameter"].sudo().set_param(self.SAVE_KEY, save_string)

    def default_get(self, fields_list=None):
        """Loads the current fields from config"""
        res = super().default_get(fields_list=fields_list or [])
        save_string = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(self.SAVE_KEY, default=False)
        )
        if save_string:
            values = save_string.split(";")
            _dict = {
                self.SAVE_FIELDS[index]: value for index, value in enumerate(values)
            }
            res.update(_dict)
        return res

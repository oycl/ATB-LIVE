from odoo import fields, models


class AbstractDatevExportColumn(models.AbstractModel):
    """Base column definition for datev and partner export configuration."""

    _name = "datev_export.abstract_column"
    _description = "Abstract Datev Column"

    header = fields.Char(default="")
    max_length = fields.Integer(default=36)
    column = fields.Char(compute="get_column")

    def get_column(self):
        """Calculate the column letter of this line, by counting columns created before this one."""
        for res in self:
            _id = res.id
            if not isinstance(_id, int):
                _id = 1000000000

            query = f"""
                SELECT COUNT(*) FROM {self._name.replace(".", "_")}
                WHERE id < {_id}
            """
            self._cr.execute(query)
            query_res = self._cr.dictfetchall()
            res.column = self.column_string(query_res[0]["count"] + 1)

    @staticmethod
    def column_string(n):
        """Generates excel column letters, A,B,C...AA,AB,..."""
        string = ""
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            string = chr(65 + remainder) + string
        return string

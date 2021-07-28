import logging

from odoo import api, models, fields


class ReconcileDatev(models.TransientModel):
    """Reconciles journal entries created by datev."""

    _name = "datev_import.reconcile"
    _description = "Wizard for importing datev people."

    only_datev = fields.Boolean("Only reconcile entries imported via datev", default=True)
    from_date = fields.Datetime("From")
    to_date = fields.Datetime("To")

    def reconcile(self, *_, **__):
        ref_mapping, name_mapping = self._get_move_lines_to_reconcile()

        for ref, lines_a in ref_mapping.items():
            lines_b = name_mapping.get(ref) or []

            for line_a in lines_a:
                for line_b in lines_b:
                    if (
                        not line_a.reconciled
                        and not line_b.reconciled
                        and line_a.account_id == line_b.account_id
                        and self.is_credit(line_a) != self.is_credit(line_b)
                    ):
                        (line_a | line_b).reconcile()
                        logging.info(f"Reconciled {line_a.move_id.name}")

    def _get_move_lines_to_reconcile(self):
        """Finds all journal entries which need to be reconciled."""
        domain = [
            ["move_id.state", "=", "posted"],
            ["reconciled", "=", False],
            ["account_id.reconcile", "=", True],
        ]

        if self.from_date and self.to_date:
            domain.append(["date", "<", self.to_date])
            domain.append(["date", ">", self.from_date])

        if self.only_datev:
            domain.append(["move_id.imported_from", "=", "datev"])

        lines = self.env["account.move.line"].search(domain)
        ref_mapping = {}
        for line in lines:
            ref = line.move_id.ref
            if ref:
                if ref not in ref_mapping:
                    ref_mapping[ref] = []
                ref_mapping[ref].append(line)

        name_mapping = {}
        for line in lines:
            name = line.move_id.name
            if name:
                if name not in name_mapping:
                    name_mapping[name] = []
                name_mapping[name].append(line)

        return ref_mapping, name_mapping

    @staticmethod
    def is_credit(line):
        return line.credit != 0.0

    def amount(self, line):
        if self.is_credit(line):
            return line.credit
        else:
            return line.debit

    def _find_related_entry(self, line):
        """Finds related journal entry to given entry."""

        return self.env["account.move.line"].search(
            [
                ["move_id.imported_from", "=", "datev"],
                ["move_id.name", "=", line.move_id.ref],
                ["move_id.state", "=", "posted"],
            ],
            limit=1,
        )

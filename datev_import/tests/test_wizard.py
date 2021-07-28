from datetime import datetime

from odoo.exceptions import UserError
from odoo.tests import tagged, common

from ..wizard.import_datev_wizard import (
    ImportWizard as ImportWizard,
    COL_UMSATZ,
    COL_KONTO,
    COL_GEGENKONTO,
    COL_SOLLHABEN,
    COL_UMSATZ_2
)

T = "datevimport"


class WizardCase(common.TransactionCase):
    konto = COL_KONTO
    gegen = COL_GEGENKONTO

    def wizard(self, **kwargs):
        return self.env[ImportWizard._name].create(kwargs)

    def _create_account(self, code):
        return self.env["account.account"].create(
            dict(
                name="test account",
                code=code,
                user_type_id=self.env["account.account.type"].browse(1).id,
                reconcile=True,
            )
        )


@tagged(T)
class TestDebitOrCredit(WizardCase):
    def test_debit_or_credit_a(self):
        dummy_line = {COL_SOLLHABEN: "S"}
        self.assertEqual(
            self.wizard()._debit_or_credit(dummy_line, is_balance_account=True),
            "debit",
        )

    def test_debit_or_credit_b(self):
        dummy_line = {COL_SOLLHABEN: "S"}
        self.assertEqual(
            self.wizard()._debit_or_credit(dummy_line, is_balance_account=False),
            "credit",
        )

    def test_debit_or_credit_c(self):
        dummy_line = {COL_SOLLHABEN: "H"}
        self.assertEqual(
            self.wizard()._debit_or_credit(dummy_line, is_balance_account=True),
            "credit",
        )

    def test_debit_or_credit_d(self):
        dummy_line = {COL_SOLLHABEN: "H"}
        self.assertEqual(
            self.wizard()._debit_or_credit(dummy_line, is_balance_account=False),
            "debit",
        )


@tagged(T)
class TestReverseAccount(WizardCase):
    def test_balance_account_name_a(self):
        import_wizard = self.wizard(balance_account=self.konto)
        self.assertEqual(import_wizard._non_balance_acc(), self.gegen)

    def test_balance_account_name_b(self):
        import_wizard = self.wizard(balance_account=self.gegen)
        self.assertEqual(import_wizard._non_balance_acc(), self.konto)


@tagged(T)
class TestGetDate(WizardCase):
    def test_get_date_a(self):
        import_wizard = self.wizard(year=2011, month=11)
        line = {"Belegdatum": "1511"}
        self.assertEqual(
            import_wizard._get_date(line), datetime(year=2011, month=11, day=15)
        )

    def test_get_date_b(self):
        import_wizard = self.wizard(year=1234, month=1)
        line = {"Belegdatum": "0101"}
        self.assertEqual(
            import_wizard._get_date(line), datetime(year=1234, month=1, day=1)
        )

    def test_get_date_c(self):
        import_wizard = self.wizard(year=2000)
        line = {"Belegdatum": "00"}
        with self.assertRaises(UserError):
            import_wizard._get_date(line)

    def test_get_date_d(self):
        import_wizard = self.wizard(year=2000)
        line = {"Belegdatum": ""}
        with self.assertRaises(UserError):
            import_wizard._get_date(line)

    def test_get_date_e(self):
        """Test that date is increased to passed month."""
        import_wizard = self.wizard(year=1234, month=2)
        line = {"Belegdatum": "0101"}
        self.assertEqual(
            import_wizard._get_date(line), datetime(year=1234, month=2, day=1)
        )


@tagged(T)
class TestGetAccount(WizardCase):
    def test_existing_account(self):
        code = "1234"
        account = self._create_account(code)
        self.assertEqual(self.wizard()._get_account_from_code(code), account)

    def test_not_existing_account(self):
        code = "123456"
        with self.assertRaises(UserError):
            self.wizard()._get_account_from_code(code)


@tagged(T)
class TestMoveType(WizardCase):
    code = 0

    def journal(self, journal_type):
        self.code += 1
        return self.env["account.journal"].create(
            dict(type=journal_type, name="", code=str(self.code))
        )

    @staticmethod
    def lines(symbol):
        return [{COL_SOLLHABEN: symbol, "Umsatz (ohne Soll/Haben-Kz)": 10}]

    def run_test(self, journal_type, symbol, balance_account, result):
        journal = self.journal(journal_type)
        lines = self.lines(symbol)
        import_wizard = self.wizard(balance_account=balance_account,)
        self.assertEqual(
            import_wizard._get_move_type(journal_id=journal, lines=lines), result
        )

    def test_sale_s_konto(self):
        self.run_test("sale", "S", self.konto, "out_invoice")

    def test_sale_s_gegen(self):
        self.run_test("sale", "S", self.gegen, "out_refund")

    def test_sale_h_gegen(self):
        self.run_test("sale", "H", self.gegen, "out_invoice")

    def test_sale_h_konto(self):
        self.run_test("sale", "H", self.konto, "out_refund")

    def test_purchase_s_konto(self):
        self.run_test("purchase", "S", self.konto, "in_refund")

    def test_purchase_s_gegen(self):
        self.run_test("purchase", "S", self.gegen, "in_invoice")

    def test_purchase_h_gegen(self):
        self.run_test("purchase", "H", self.gegen, "in_refund")

    def test_purchase_h_konto(self):
        self.run_test("purchase", "H", self.konto, "in_invoice")


@tagged(T)
class TestValidateLine(WizardCase):
    @staticmethod
    def _line(umsatz, symbol, konto, gegenkonto):
        return {
            COL_UMSATZ: umsatz,
            COL_SOLLHABEN: symbol,
            COL_KONTO: konto,
            COL_GEGENKONTO: gegenkonto,
            COL_UMSATZ_2: ""
        }

    def test_validate_valid_line(self):
        self._create_account("12345")
        self._create_account("54321")
        line = self._line("10", "S", "12345", "54321")
        self.wizard()._convert_and_validate_line(line)
        self.assertEqual(line, {**line, COL_UMSATZ: 10})

    def test_validate_valid_line_comma(self):
        self._create_account("12345")
        self._create_account("54321")
        line = self._line("10,3", "S", "12345", "54321")
        self.wizard()._convert_and_validate_line(line)
        self.assertEqual(line, {**line, COL_UMSATZ: 10.3})

    def test_validate_line_wrong_value(self):
        self._create_account("12345")
        self._create_account("54321")
        line = self._line("A", "S", "12345", "54321")
        with self.assertRaises(UserError):
            self.wizard()._convert_and_validate_line(line)

    def test_validate_line_wrong_symbol(self):
        self._create_account("12345")
        self._create_account("54321")
        line = self._line("10", "X", "12345", "54321")
        with self.assertRaises(UserError):
            self.wizard()._convert_and_validate_line(line)

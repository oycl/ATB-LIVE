from odoo.tests import common, tagged
from unittest import skip

T = "datevimport"


@skip("not working")
@tagged(T)
class TestMenuButton(common.HttpCase):
    def test_button(self):
        url = "/web#model=account.journal&view_type=kanban"
        code = """
        let item = document.querySelectorAll('nav.o_main_navbar');
        console.log("---------------------");
        console.log(document.querySelectorAll("body")[0].outerHTML);
        document.getElementById(item).click();
        console.log('test successful');
        """
        self.phantom_js(url, code, login="admin")

from datetime import datetime

from odoo.exceptions import UserError
from odoo.tests import tagged, common

from ..wizard.import_people_wizard import ImportPeopleWizard

T = "datevimport"


class WizardCase(common.TransactionCase):
    def wizard(self, **kwargs):
        return self.env[ImportPeopleWizard._name].create(kwargs)


# @tagged(T)
# class TestValidateLine(WizardCase):
#     def test_

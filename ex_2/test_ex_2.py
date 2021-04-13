import unittest
from ex_2.services import BankingService
from ex_2.models import Banking


class BankingTest(unittest.TestCase):
    service = BankingService()

    def test_1(self):
        banking = Banking(is_vip=True)
        fees = self.service.get_banking_fees(banking)
        self.assertEqual(fees, 0)

    def test_2(self):
        banking = Banking(is_day_off=True)
        fees = self.service.get_banking_fees(banking)
        self.assertEqual(fees, 110)

    def test_3(self):
        banking = Banking(is_day_off=False, is_time=True)
        fees = self.service.get_banking_fees(banking)
        self.assertEqual(fees, 0)

    def test_4(self):
        banking = Banking(is_day_off=False, is_time=False)
        fees = self.service.get_banking_fees(banking)
        self.assertEqual(fees, 110)

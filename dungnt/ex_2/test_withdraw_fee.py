import unittest
from dungnt.ex_2.models import ATMWithdraw
from datetime import datetime

class test_withdraw_fee(unittest.TestCase):
    # vip

    def test_vip_normal_day_free_hour(self):
        atm_withdraw = ATMWithdraw(True, datetime.strptime("08/04/21 16:30", "%d/%m/%y %H:%M"))
        self.assertEqual(atm_withdraw.get_withdraw_fee(), 0)

    # ko vip
    def test_no_vip_normal_day_free_hour(self):
        atm_withdraw = ATMWithdraw(False, datetime.strptime("08/04/21 16:30", "%d/%m/%y %H:%M"))
        self.assertEqual(atm_withdraw.get_withdraw_fee(), 0)

    def test_no_vip_normal_day_free_hour_boundary_1(self):
        atm_withdraw = ATMWithdraw(False, datetime.strptime("08/04/21 8:45", "%d/%m/%y %H:%M"))
        self.assertEqual(atm_withdraw.get_withdraw_fee(), 0)

    def test_no_vip_normal_day_have_fee_hour_1(self):
        atm_withdraw = ATMWithdraw(False, datetime.strptime("08/04/21 19:30", "%d/%m/%y %H:%M"))
        self.assertEqual(atm_withdraw.get_withdraw_fee(), 110)

    def test_no_vip_normal_day_have_fee_hour_2(self):
        atm_withdraw = ATMWithdraw(False, datetime.strptime("08/04/21 6:30", "%d/%m/%y %H:%M"))
        self.assertEqual(atm_withdraw.get_withdraw_fee(), 110)

    def test_no_vip_normal_day_free_hour_boundary_2(self):
        atm_withdraw = ATMWithdraw(False, datetime.strptime("08/04/21 18:00", "%d/%m/%y %H:%M"))
        self.assertEqual(atm_withdraw.get_withdraw_fee(), 110)

    def test_no_vip_weekend(self): #thu 7
        atm_withdraw = ATMWithdraw(False, datetime.strptime("10/04/21 16:30", "%d/%m/%y %H:%M"))
        self.assertEqual(atm_withdraw.get_withdraw_fee(), 110)

    def test_no_vip_weekend_1(self): #thu 7
        atm_withdraw = ATMWithdraw(False, datetime.strptime("10/04/21 16:30", "%d/%m/%y %H:%M"))
        self.assertEqual(atm_withdraw.get_withdraw_fee(), 110)

    def test_no_vip_hoiliday(self):  # thu 30/4
        atm_withdraw = ATMWithdraw(False, datetime.strptime("30/04/21 16:30", "%d/%m/%y %H:%M"))
        self.assertEqual(atm_withdraw.get_withdraw_fee(), 110)


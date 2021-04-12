import unittest
from dungnt.ex1.models import Beer

class KeangNam_Beer_Test_Fee(unittest.TestCase):

    def test_in_time_no_voucher(self):
        beer = Beer(1, '16:30', False)
        self.assertEqual(beer.caculate_price_order(), 290)

    def test_in_time_no_voucher_2(self):
        beer = Beer(2, '16:30', False)
        self.assertEqual(beer.caculate_price_order(), 580)

    def test_in_time_has_voucher(self):
        beer = Beer(1, '16:30', True)
        self.assertEqual(beer.caculate_price_order(), 100)

    def test_in_time_has_voucher_2(self):
        beer = Beer(2, '16:30', True)
        self.assertEqual(beer.caculate_price_order(), 390)

    def test_not_in_time_no_voucher(self):
        beer = Beer(1, '18:30', False)
        self.assertEqual(beer.caculate_price_order(), 490)

    def test_not_in_time_no_voucher_2(self):
        beer = Beer(2, '18:30', False)
        self.assertEqual(beer.caculate_price_order(), 980)

    def test_not_in_time_has_voucher(self):
        beer = Beer(1, '18:30', True)
        self.assertEqual(beer.caculate_price_order(), 100)

    def test_not_in_time_has_voucher_2(self):
        beer = Beer(2, '18:30', True)
        self.assertEqual(beer.caculate_price_order(), 590)

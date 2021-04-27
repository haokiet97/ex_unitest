import unittest
from ex_7.services import ShoppingService
from ex_7.models import Shopping


class ShoppingTest(unittest.TestCase):
    shopping = ShoppingService()

    def test_1(self):
        shopping = Shopping(is_total=True)
        fee = self.shopping.get_fee(shopping)
        self.assertEqual(fee, 0)

    def test_6(self):
        shopping = Shopping(is_total=True, is_vip=False, is_ship_now=True)
        fee = self.shopping.get_fee(shopping)
        self.assertEqual(fee, 500)

    def test_2(self):
        shopping = Shopping(is_total=True, is_vip=True)
        fee = self.shopping.get_fee(shopping)
        self.assertEqual(fee, 0)

    def test_3(self):
        shopping = Shopping(is_total=True, is_vip=True, is_ship_now=True)
        fee = self.shopping.get_fee(shopping)
        self.assertEqual(fee, 500)

    def test_4(self):
        shopping = Shopping(is_total=False, is_vip=True)
        fee = self.shopping.get_fee(shopping)
        self.assertEqual(fee, 0)

    def test_5(self):
        shopping = Shopping(is_total=False, is_vip=False)
        fee = self.shopping.get_fee(shopping)
        self.assertEqual(fee, 500)

    def test_6(self):
        shopping = Shopping(is_total=False, is_vip=False, is_ship_now=True)
        fee = self.shopping.get_fee(shopping)
        self.assertEqual(fee, 1000)

    def test_7(self):
        shopping = Shopping(is_total=False, is_vip=True, is_ship_now=True)
        fee = self.shopping.get_fee(shopping)
        self.assertEqual(fee, 500)





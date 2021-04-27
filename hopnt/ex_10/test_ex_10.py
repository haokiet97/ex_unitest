import unittest
from hopnt.ex_10.services import ShoppingService
from hopnt.ex_10.models import Shopping


class ShoppingTest(unittest.TestCase):
    shopping = ShoppingService()

    def test_sliver_3000(self):
        shopping = Shopping(sliver=True, money=3000)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '1%')

    def test_sliver_5000_lucky(self):
        shopping = Shopping(sliver=True, money=5000, lucky=True)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '2%, coupon')

    def test_sliver_5000_not_lucky(self):
        shopping = Shopping(sliver=True, money=5000, lucky=False)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '2%')

    def test_sliver_10000_lucky(self):
        shopping = Shopping(sliver=True, money=10000, lucky=True)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '4%, coupon')

    def test_sliver_10000_not_lucky(self):
        shopping = Shopping(sliver=True, money=10000, lucky=False)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '4%')

    def test_gold_3000(self):
        shopping = Shopping(gold=True, money=3000)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '3%')

    def test_gold_5000_lucky(self):
        shopping = Shopping(gold=True, money=5000, lucky=True)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '5%, coupon')

    def test_gold_5000_not_lucky(self):
        shopping = Shopping(gold=True, money=5000, lucky=False)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '5%')

    def test_gold_10000_lucky(self):
        shopping = Shopping(gold=True, money=10000, lucky=True)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '10%, coupon')

    def test_gold_10000_not_lucky(self):
        shopping = Shopping(sliver=True, money=10000, lucky=False)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '10%')

    def test_black_3000(self):
        shopping = Shopping(black=True, money=3000)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '5%')

    def test_black_5000_lucky(self):
        shopping = Shopping(black=True, money=5000, lucky=True)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '7%, coupon')

    def test_black_5000_not_lucky(self):
        shopping = Shopping(black=True, money=5000, lucky=False)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '7%')

    def test_black_10000_lucky(self):
        shopping = Shopping(black=True, money=10000, lucky=True)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '15%, coupon')

    def test_black_10000_not_lucky(self):
        shopping = Shopping(black=True, money=10000, lucky=False)
        fee = self.shopping.get_endows(shopping)
        self.assertEqual(fee, '15%')

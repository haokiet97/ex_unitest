import unittest
from ex_5.services import OrderService
from ex_5.models import Order


class OrderTest(unittest.TestCase):
    order = OrderService()

    def test_1(self):
        order = Order(is_total=True, is_ship=True)
        voucher = self.service.get_vouchers(order)
        self.assertEqual(voucher, ['POTATO', 'PIZZA'])

    def test_2(self):
        order = Order(is_total=True, is_ship=False, has_coupon=True)
        voucher = self.service.get_vouchers(order)
        self.assertEqual(voucher, ['POTATO', 'DISCOUNT'])


    def test_3(self):
        order = Order(is_total=True, is_ship=False, has_coupon=False)
        voucher = self.service.get_vouchers(order)
        self.assertEqual(voucher, ['POTATO'])

    def test_4(self):
        order = Order(is_total=False, is_ship=True)
        voucher = self.service.get_vouchers(order)
        self.assertEqual(voucher, ['PIZZA'])

    def test_5(self):
        order = Order(is_total=False, is_ship=False, has_coupon=True)
        voucher = self.service.get_vouchers(order)
        self.assertEqual(voucher, ['DISCOUNT'])

    def test_6(self):
        order = Order(is_total=True, is_ship=False, has_coupon=False)
        voucher = self.service.get_vouchers(order)
        self.assertEqual(voucher, [])


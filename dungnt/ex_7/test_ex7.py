import unittest
from .models import ShippingFee


class TestShippingFee(unittest.TestCase):
    def test_normal_ship_money_greater_than_5000(self):
        ship = ShippingFee(5500)
        self.assertEqual(0, ship.calculate_shipping_fee())

    def test_normal_ship_money_is_premium_mem(self):
        ship = ShippingFee(2500, False, True)
        self.assertEqual(0, ship.calculate_shipping_fee())

    def test_normal_ship_money_is_not_premium_mem_money_less_than_5000(self):
        ship = ShippingFee(2500, False, False)
        self.assertEqual(500, ship.calculate_shipping_fee())

    def test_normal_ship_money_is_premium_mem_money_greater_than_5000(self):
        ship = ShippingFee(5500, False, True)
        self.assertEqual(0, ship.calculate_shipping_fee())

    def test_fast_ship_money_greater_than_5000(self):
        ship = ShippingFee(5500, True)
        self.assertEqual(500, ship.calculate_shipping_fee())

    def test_fast_ship_money_is_premium_mem(self):
        ship = ShippingFee(2500, True, True)
        self.assertEqual(500, ship.calculate_shipping_fee())

    def test_fast_ship_money_is_not_premium_mem_money_less_than_5000(self):
        ship = ShippingFee(2500, True, False)
        self.assertEqual(1000, ship.calculate_shipping_fee())

    def test_fast_ship_money_is_premium_mem_money_greater_than_5000(self):
        ship = ShippingFee(5500, True, False)
        self.assertEqual(500, ship.calculate_shipping_fee())

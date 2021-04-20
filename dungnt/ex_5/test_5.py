import unittest
from .models import Pizza


class TestPizzaInvoice(unittest.TestCase):

    def test_greater_than_1500_no_shipping(self):
        pizza = Pizza(1600, False)
        self.assertEqual({'has_potato_chips': True, 'free_pizza': True, 'discount_20_per': False},
                         pizza.check_calculate_invoice())

    def test_greater_than_1500_shipping_has_coupon(self):
        pizza = Pizza(1600, True, True)
        self.assertEqual({'has_potato_chips': True, 'free_pizza': False, 'discount_20_per': True},
                         pizza.check_calculate_invoice())

    def test_greater_than_1500_shipping_has_no_coupon(self):
        pizza = Pizza(1600, True, False)
        self.assertEqual({'has_potato_chips': True, 'free_pizza': False, 'discount_20_per': False},
                         pizza.check_calculate_invoice())

    def test_less_than_1500_no_shipping(self):
        pizza = Pizza(1400)
        self.assertEqual({'has_potato_chips': False, 'free_pizza': True, 'discount_20_per': False},
                         pizza.check_calculate_invoice())

    def test_less_than_1500_shipping_has_coupon(self):
        pizza = Pizza(1600, True, True)
        self.assertEqual({'has_potato_chips': True, 'free_pizza': False, 'discount_20_per': True},
                         pizza.check_calculate_invoice())

    def test_less_than_1500_shipping_has_no_coupon(self):
        pizza = Pizza(1600, True, False)
        self.assertEqual({'has_potato_chips': True, 'free_pizza': False, 'discount_20_per': False},
                         pizza.check_calculate_invoice())


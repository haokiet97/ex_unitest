import unittest
from ex_1.services import BeerService
from ex_1.models import Beer


class BeerTest(unittest.TestCase):
    service = BeerService()

    def test_1(self):
        beer = Beer(has_voucher=True)
        amount = self.service.get_beer_amount(beer)
        self.assertEqual(amount, 100)

    def test_2(self):
        beer = Beer(time='17:00')
        amount = self.service.get_beer_amount(beer)
        self.assertEqual(amount, 290)

    def test_3(self):
        beer = Beer(time='13:00')
        amount = self.service.get_beer_amount(beer)
        self.assertEqual(amount, 490)

    def test_4(self):
        beer = Beer(time='16:00')
        amount = self.service.get_beer_amount(beer)
        self.assertEqual(amount, 290)

    def test_5(self):
        beer = Beer(time='17:59')
        amount = self.service.get_beer_amount(beer)
        self.assertEqual(amount, 290)

    def test_6(self):
        beer = Beer(time='18:00')
        amount = self.service.get_beer_amount(beer)
        self.assertEqual(amount, 490)

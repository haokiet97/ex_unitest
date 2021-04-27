import unittest
from hopnt.ex_8.services import BadmintonYardService
from hopnt.ex_8.models import BadmintonYard


class BadmintonYardTest(unittest.TestCase):
    service = BadmintonYardService()

    def test_young(self):
        user = BadmintonYard(age=10)
        fee = self.service.get_fee_yard(user)
        self.assertEqual(fee, 900)

    def test_tuesday(self):
        user = BadmintonYard(day='tue')
        fee = self.service.get_fee_yard(user)
        self.assertEqual(fee, 1200)

    def test_is_female_and_friday(self):
        user = BadmintonYard(is_female=True, day='fri')
        fee = self.service.get_fee_yard(user)
        self.assertEqual(fee, 1400)

    def test_is_female_and_not_friday(self):
        user = BadmintonYard(is_female=True, day='thu', age=40)
        fee = self.service.get_fee_yard(user)
        self.assertEqual(fee, 1800)

    def test_is_not_female_and_not_friday_and_young(self):
        user = BadmintonYard(is_female=False, day='thu', age=40)
        fee = self.service.get_fee_yard(user)
        self.assertEqual(fee, 1800)

    # def test_is_not_female_and_friday(self):
    #     user = BadmintonYard(is_female=False, day='fri', age=40)
    #     fee = self.service.get_fee_yard(user)
    #     self.assertEqual(fee, 1800)

    def test_is_female_and_not_friday_and_old(self):
        user = BadmintonYard(is_female=True, day='thu', age=70)
        fee = self.service.get_fee_yard(user)
        self.assertEqual(fee, 1600)

    def test_not_is_female_and_not_friday_and_old(self):
        user = BadmintonYard(is_female=False, day='thu', age=70)
        fee = self.service.get_fee_yard(user)
        self.assertEqual(fee, 1600)

    # def test_is_not_female_and_friday_and_old(self):
    #     user = BadmintonYard(is_female=False, day='fri', age=70)
    #     fee = self.service.get_fee_yard(user)
    #     self.assertEqual(fee, 1600)

    def test_is_so_young(self):
        user = BadmintonYard(age=-1)
        fee = self.service.get_fee_yard(user)
        self.assertEqual(fee, -1)

    def test_is_so_old(self):
        user = BadmintonYard(age=121)
        fee = self.service.get_fee_yard(user)
        self.assertEqual(fee, -1)

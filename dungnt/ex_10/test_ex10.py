import unittest
from .models import BonusPrepaidCard


class TestBonusPrepaidCard(unittest.TestCase):
    def test_has_no_bonus(self):
        bonus_prepaid_card = BonusPrepaidCard(1000)
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 0, 'has_lottery': False})

    def test_gl_10000_sliver(self):
        bonus_prepaid_card = BonusPrepaidCard(11000)
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 4, 'has_lottery': True})

    def test_gl_5000_sliver(self):
        bonus_prepaid_card = BonusPrepaidCard(6000)
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 2, 'has_lottery': True})

    def test_gl_3000_sliver(self):
        bonus_prepaid_card = BonusPrepaidCard(4000)
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 1, 'has_lottery': False})

    def test_gl_10000_gold(self):
        bonus_prepaid_card = BonusPrepaidCard(11000, "gold")
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 10, 'has_lottery': True})

    def test_gl_5000_gold(self):
        bonus_prepaid_card = BonusPrepaidCard(6000, "gold")
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 5, 'has_lottery': True})

    def test_gl_3000_gold(self):
        bonus_prepaid_card = BonusPrepaidCard(4000, "gold")
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 3, 'has_lottery': False})

    def test_gl_10000_black(self):
        bonus_prepaid_card = BonusPrepaidCard(11000, "black")
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 15, 'has_lottery': True})

    def test_gl_5000_black(self):
        bonus_prepaid_card = BonusPrepaidCard(6000, "black")
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 7, 'has_lottery': True})

    def test_gl_3000_black(self):
        bonus_prepaid_card = BonusPrepaidCard(4000, "black")
        self.assertEqual(bonus_prepaid_card.calculate_bonus_percent(), {'discount_percent': 5, 'has_lottery': False})

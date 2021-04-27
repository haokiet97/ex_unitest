import unittest
from .models import PlayingBadmintonFee


class TestPlayBadmintonFee(unittest.TestCase):
    def test_tuesday(self):
        badminton_fee = PlayingBadmintonFee(1, True, "tues")
        self.assertEqual(badminton_fee.calculate_fee(), 1200)

    def test_old_lt_0(self):
        badminton_fee = PlayingBadmintonFee(-1)
        self.assertEqual(badminton_fee.calculate_fee(), -1)

    def test_old_gt_120(self):
        badminton_fee = PlayingBadmintonFee(121)
        self.assertEqual(badminton_fee.calculate_fee(), -1)

    def test_children_fee(self):
        badminton_fee = PlayingBadmintonFee(12)
        self.assertEqual(badminton_fee.calculate_fee(), 900)

    def test_is_women_and_friday_gt_13(self):
        badminton_fee = PlayingBadmintonFee(30, True, "fri")
        self.assertEqual(badminton_fee.calculate_fee(), 1400)

    def test_is_women_and_friday_lt_13(self):
        badminton_fee = PlayingBadmintonFee(12, True, "fri")
        self.assertEqual(badminton_fee.calculate_fee(), 900)

    def test_is_women_and_friday_gt_65(self):
        badminton_fee = PlayingBadmintonFee(70, True, "fri")
        self.assertEqual(badminton_fee.calculate_fee(), 1400)

    def test_old_fee(self):
        badminton_fee = PlayingBadmintonFee(70)
        self.assertEqual(badminton_fee.calculate_fee(), 1600)

    def test_adult_fee(self):
        badminton_fee = PlayingBadmintonFee(30, False)
        self.assertEqual(badminton_fee.calculate_fee(), 1800)




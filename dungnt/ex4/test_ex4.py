import unittest
from dungnt.ex4.models import Color

class Generator_Color_Test(unittest.TestCase):

    def test_is_holiday(self):
        color = Color(True)
        self.assertEqual(color.get_color(), "red")

    def test_is_sunday(self):
        color = Color(False, True)
        self.assertEqual(color.get_color(), "red")

    def test_is_sunday_and_holiday(self):
        color = Color(True, True)
        self.assertEqual(color.get_color(), "red")

    def test_is_saturday(self):
        color = Color(False, False, True)
        self.assertEqual(color.get_color(), "blue")

    def test_is_saturday_and_holiday(self):
        color = Color(True, False, True)
        self.assertEqual(color.get_color(), "red")

    def test_is_normal_day(self):
        color = Color(False, False, False)
        self.assertEqual(color.get_color(), "black")

import unittest
from ex_4.services import DayColorService
from ex_4.models import DayColor


class DayTest(unittest.TestCase):
    service = DayColorService()

    def test_1(self):
        order = DayColor(is__holiday=True, is_weekday=True)
        color = self.service.get_day_color(order)
        self.assertEqual(color, 'red')

    def test_2(self):
        order = DayColor(is__holiday=True, is_sunday=True)
        color = self.service.get_day_color(order)
        self.assertEqual(color, 'red')

    def test_3(self):
        order = DayColor(is__holiday=True, is_saturday=True)
        color = self.service.get_day_color(order)
        self.assertEqual(color, 'red')

    def test_4(self):
        order = DayColor(is_sunday=True)
        color = self.service.get_day_color(order)
        self.assertEqual(color, 'red')

    def test_5(self):
        order = DayColor(is_saturday=True)
        color = self.service.get_day_color(order)
        self.assertEqual(color, 'blue')

    def test_6(self):
        order = DayColor(is_weekday=True)
        color = self.service.get_day_color(order)
        self.assertEqual(color, 'black')

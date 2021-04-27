import unittest
from ex_6.services import ParkingService
from ex_6.models import Parking


class ParkingTest(unittest.TestCase):
    parking = ParkingService()

    def test_1(self):
        parking = Order(total=5000, film=False)
        free_time = self.service.get_free_time_parking(parking)
        self.assertEqual(free_time, 120)

    def test_2(self):
        parking = Order(total=5000, film=True)
        free_time = self.service.get_free_time_parking(parking)
        self.assertEqual(free_time, 120+180)

    def test_3(self):
        parking = Order(total=2000, film=False)
        free_time = self.service.get_free_time_parking(parking)
        self.assertEqual(free_time, 60)

    def test_4(self):
        parking = Order(total=2000, film=True)
        free_time = self.service.get_free_time_parking(parking)
        self.assertEqual(free_time, 60+180)

    def test_5(self):
        parking = Order(total=1000, film=False)
        free_time = self.service.get_free_time_parking(parking)
        self.assertEqual(free_time, 0)

    def test_6(self):
        parking = Order(total=1000, film=True)
        free_time = self.service.get_free_time_parking(parking)
        self.assertEqual(free_time, 180)

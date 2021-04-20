import unittest
from .models import ParkingFee


class TestParkingFee(unittest.TestCase):
    def test_watch_film_money_greater_than_5000(self):
        parking_fee = ParkingFee(5500, True)
        self.assertEqual(300, parking_fee.calculate_free_time_parking())

    def test_watch_film_money_greater_than_2000(self):
        parking_fee = ParkingFee(2500, True)
        self.assertEqual(240, parking_fee.calculate_free_time_parking())

    def test_watch_film_money_less_than_2000(self):
        parking_fee = ParkingFee(1500, True)
        self.assertEqual(180, parking_fee.calculate_free_time_parking())

    def test_no_watch_film_money_greater_than_5000(self):
        parking_fee = ParkingFee(5500)
        self.assertEqual(120, parking_fee.calculate_free_time_parking())

    def test_no_watch_film_money_greater_than_2000(self):
        parking_fee = ParkingFee(2500)
        self.assertEqual(60, parking_fee.calculate_free_time_parking())

    def test_no_watch_film_money_less_than_2000(self):
        parking_fee = ParkingFee(1000)
        self.assertEqual(0, parking_fee.calculate_free_time_parking())

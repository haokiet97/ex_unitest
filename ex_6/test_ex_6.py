import unittest
from ex_6.services import ShoppingOrderService, FREE_TIME_BY_WATCH_MOVIE, FREE_TIME_BY_TOTAL_CASH, \
    FREE_TIME_BY_TOTAL_CASH_BIG
from ex_6.models import ShoppingOrder


class ShoppingOrderTest(unittest.TestCase):
    service = ShoppingOrderService()

    def test_no_free_time_parking(self):
        shopping_order = ShoppingOrder()
        free_parking_time = self.service.get_free_time_parking(shopping_order)
        self.assertEqual(free_parking_time, 0)

    def test_free_parking_time_with_no_watching_movie_total_cash_in_2000_5000(self):
        shopping_order = ShoppingOrder(total_cash=2001)
        free_parking_time = self.service.get_free_time_parking(shopping_order)
        self.assertEqual(free_parking_time, FREE_TIME_BY_TOTAL_CASH)

    def test_free_parking_time_with_no_watching_movie_total_cash_gte_5000(self):
        shopping_order = ShoppingOrder(total_cash=5001)
        free_parking_time = self.service.get_free_time_parking(shopping_order)
        self.assertEqual(free_parking_time, FREE_TIME_BY_TOTAL_CASH_BIG)

    def test_free_parking_time_with_only_watching_movie(self):
        shopping_order = ShoppingOrder(is_watching_movie=True)
        free_parking_time = self.service.get_free_time_parking(shopping_order)
        self.assertEqual(free_parking_time, FREE_TIME_BY_WATCH_MOVIE)

    def test_free_parking_time_with_watching_movie_total_cash_in_2000_5000(self):
        shopping_order = ShoppingOrder(is_watching_movie=True, total_cash=4999)
        free_parking_time = self.service.get_free_time_parking(shopping_order)
        self.assertEqual(free_parking_time, FREE_TIME_BY_WATCH_MOVIE + FREE_TIME_BY_TOTAL_CASH)

    def test_free_parking_time_with_watching_movie_total_cash_gte_5000(self):
        shopping_order = ShoppingOrder(is_watching_movie=True, total_cash=5001)
        free_parking_time = self.service.get_free_time_parking(shopping_order)
        self.assertEqual(free_parking_time, FREE_TIME_BY_WATCH_MOVIE + FREE_TIME_BY_TOTAL_CASH_BIG)

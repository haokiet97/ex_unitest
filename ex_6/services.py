FREE_TIME_BY_WATCH_MOVIE = 180
FREE_TIME_BY_TOTAL_CASH = 60
FREE_TIME_BY_TOTAL_CASH_BIG = 120


class ShoppingOrderService:
    free_time_parking = 0

    def get_free_time_parking(self, shopping_order=None):
        self.free_time_parking = 0
        if not shopping_order:
            return 0
        if shopping_order.is_watching_movie:
            self.free_time_parking += FREE_TIME_BY_WATCH_MOVIE
        if 2000 <= shopping_order.total_cash < 5000:
            self.free_time_parking += 60
        if shopping_order.total_cash >= 5000:
            self.free_time_parking += 120
        return self.free_time_parking

    def not_use_this_method(self):
        print(self.free_time_parking)






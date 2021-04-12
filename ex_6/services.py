FREE_TIME_BY_WATCH_MOVIE = 180
FREE_TIME_BY_TOTAL_CASH = 60
FREE_TIME_BY_TOTAL_CASH_BIG = 120


class ShoppingOrderService:
    free_time_parking = 0

    def get_free_time_parking(self, shopping_order=None):
        if not shopping_order:
            return 0
        if shopping_order.is_watching_movie:
            self.free_time_parking += FREE_TIME_BY_WATCH_MOVIE






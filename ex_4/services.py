from .models import DayColor


class DayColorService:
    def get_day_color(self, order: DayColor) -> int:
        return order.get_color()

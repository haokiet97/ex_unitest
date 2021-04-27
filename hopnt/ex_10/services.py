from .models import Shopping


class ShoppingService:
    def get_endows(self, order: Shopping) -> int:
        return order.get_endow()

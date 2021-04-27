from .models import Shopping


class ShoppingService:
    def get_fee(self, order: Order) -> int:
        return order.get_fee_ship()

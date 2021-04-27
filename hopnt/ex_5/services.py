from .models import Order


class OrderService:
    def get_vouchers(self, order: Order) -> int:
        return order.get_voucher()

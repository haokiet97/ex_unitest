class ShippingFee:
    def __init__(self, money_invoice, shipping_method_fast=False, is_premium_member=False):
        self.money_invoice = money_invoice
        self.shipping_method_fast = shipping_method_fast
        self.is_premium_member = is_premium_member

    def calculate_shipping_fee(self):
        shipping_fee = 500
        if self.shipping_method_fast:
            shipping_fee += 500
        if self.is_premium_member or self.money_invoice > 5000:
            shipping_fee -= 500
        return shipping_fee

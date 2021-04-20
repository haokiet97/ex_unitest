class Pizza:
    def __init__(self, total_invoice, is_shipping=False, has_coupon=False):
        self.total_invoice = total_invoice
        self.is_shipping = is_shipping
        self.has_coupon = has_coupon

    def check_calculate_invoice(self):
        result = {'has_potato_chips': False, 'free_pizza': False, 'discount_20_per': False}
        if self.total_invoice > 1500:
            result.has_potato_chips = True
        if not self.is_shipping:
            result.free_pizza = True
        elif self.is_shipping and self.has_coupon:
            result.discount_20_per = True
        return result

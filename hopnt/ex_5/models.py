
class Order:

    def __init__(self, is_total=False, is_ship=False, has_coupon=False, has_voucher=[]):
        self.is_total = is_total
        self.is_ship = is_ship
        self.has_coupon = has_coupon
        self.has_voucher = has_voucher

    def get_voucher(self):
        if self.is_total:
            self.has_voucher.append('POTATO')
        if self.is_ship:
            if self.has_coupon:
               self.has_voucher.append('DISCOUNT')
        else:
            self.has_voucher.append('PIZZA')
        return self.has_voucher


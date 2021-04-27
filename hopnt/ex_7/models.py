
class Shopping:

    def __init__(self, is_total=False, is_vip=False, is_ship_now=False):
        self.is_total = is_total
        self.is_vip = is_vip
        self.is_ship_now = is_ship_now

    def get_fee_ship(self):
        fee_normal = 500
        fee_ship_now = 0
        if self.is_vip or self.is_total:
            fee_normal = 0
        if self.is_ship_now:
            fee_ship_now = 500
        return fee_ship_now + fee_normal





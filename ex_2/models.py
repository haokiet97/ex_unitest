
class Banking:

    def __init__(self, is_vip=False, is_day_off=False, is_time=False):
        self.is_vip = is_vip
        self.is_day_off = is_day_off
        self.is_time = is_time

    def get_fees(self):
        if self.is_vip:
            return 0
        else:
            if self.is_day_off:
                return 110
            else:
                if self.is_time:
                    return 0
                else:
                    return 110

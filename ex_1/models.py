
class Beer:

    def __init__(self, time='00:00', has_voucher=False):
        self.has_voucher = has_voucher
        self.time = time

    def get_amount(self):
        if self.has_voucher:
            return 100
        else:
            time = int(self.time.split(':')[0]) * 60 + int(self.time.split(':')[1])
            if time - 960 >= 0 and 1080 - time > 0:
                return 290
            else:
                return 490

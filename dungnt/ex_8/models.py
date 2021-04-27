class PlayingBadmintonFee:
    def __init__(self, old=0, is_women=False, weekday='mon'):
        self.old = old
        self.is_women = is_women
        self.weekday = weekday

    def calculate_fee(self):
        fee = 1800
        if self.old < 0 or self.old > 120:
            return -1
        if self.weekday == 'tues':
            return 1200
        else:
            if self.old < 13:
                fee = 900
            elif self.is_women and self.weekday == 'fri':
                fee = 1400
            elif self.old > 65:
                fee = 1600
        return fee


class BadmintonYard:

    def __init__(self, age=0, is_female=False, day='mon'):
        self.age = age
        self.is_female = is_female
        self.day = day

    def get_fee(self):
        if self.age < 0 or self.age > 120:
            return -1
        elif self.age < 13:
            return 900
        elif self.day == 'tue':
            return 1200
        elif self.is_female is True and self.day == 'fri':
            return 1400
        elif self.age > 65:
            return 1600
        return 1800



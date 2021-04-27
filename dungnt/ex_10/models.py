class BonusPrepaidCard:

    def __init__(self, money, grade="sliver"):
        self.money = money
        self.grade = grade

    def calculate_bonus_percent(self):
        bonus = {'discount_percent': 0, 'has_lottery': False}
        if self.money > 10000:
            bonus["has_lottery"] = True
            if self.grade == "black":
                bonus['discount_percent'] = 15
            elif self.grade == "gold":
                bonus['discount_percent'] = 10
            else:
                bonus['discount_percent'] = 4
        elif self.money > 5000:
            bonus["has_lottery"] = True
            if self.grade == "black":
                bonus['discount_percent'] = 7
            elif self.grade == "gold":
                bonus['discount_percent'] = 5
            else:
                bonus['discount_percent'] = 2
        elif self.money > 3000:
            if self.grade == "black":
                bonus['discount_percent'] = 5
            elif self.grade == "gold":
                bonus['discount_percent'] = 3
            else:
                bonus['discount_percent'] = 1
        return bonus

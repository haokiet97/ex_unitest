class Shopping:

    def __init__(self, sliver=False, gold=False, black=False, money=0, lucky=False):
        self.sliver = sliver
        self.gold = gold
        self.black = black
        self.money = money
        self.lucky = lucky

    def get_endow(self):
        if self.sliver:
            if self.money == '3000':
                return '1%'
            elif self.money == '5000':
                if self.lucky:
                    return '2%, coupon'
                return '2%'
            elif self.money == '10000':
                if self.lucky:
                    return '4%, coupon'
                return '4%'

        elif self.gold:
            if self.money == '3000':
                return '3%'
            elif self.money == '5000':
                if self.lucky:
                    return '5%, coupon'
                return '5%'
            elif self.money == '10000':
                if self.lucky:
                    return '10%, coupon'
                return '10%'

        elif self.sliver:
            if self.money == '3000':
                return '5%'
            elif self.money == '5000':
                if self.lucky:
                    return '7%, coupon'
                return '7%'
            elif self.money == '10000':
                if self.lucky:
                    return '15%, coupon'
                return '15%'

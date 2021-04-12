from datetime import datetime

class Beer:
    price = 0
    def __init__(self, number, time , has_voucher):
        self.number = number
        time_buy = datetime.strptime(time, '%H:%M').time()
        self.in_time = 16 <= time_buy.hour and time_buy.hour < 18
        self.has_voucher = has_voucher

    def caculate_price_order(self):
        price_a_cup_of_beer = 490
        if self.in_time:
            price_a_cup_of_beer = 290
        if self.has_voucher:
            self.price = 100 + (self.number - 1)*price_a_cup_of_beer
        else:
            self.price = self.number * price_a_cup_of_beer
        return self.price

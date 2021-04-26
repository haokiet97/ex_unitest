from ex_8.models import *

TUESDAY_PRICE = 1200
FRIDAY_FEMALE_PRICE = 1400
OLD_PEOPLE_PRICE = 1600
NORMAL_PRICE = 1800


class TicketService:
    normal_price = NORMAL_PRICE

    def calc_price(self, player: Player, day_in_week=0):
        price = self.normal_price
        if player.age not in range(0, 121):
            raise Exception("Error")
        if player.age < 13:
            price = self.normal_price / 2


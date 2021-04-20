
class ParkingFee:
    def __init__(self, total_money, watch_film=False):
        self. total_money = total_money
        self.watch_film = watch_film

    def calculate_free_time_parking(self):
        free_minutes = 0
        if self.watch_film:
            self.total_money += self.total_money + 1 #cong them tien xem phim
            free_minutes += 180
        if self.total_money > 5000:
            free_minutes += 120
        elif self.total_money > 2000:
            free_minutes += 60
        return free_minutes




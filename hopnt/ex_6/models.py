
class Parking:

    def __init__(self, total=0, film=False, free_time=0):
        self.total = total
        self.film = film


    def get_parking_time(self):
        if self.total >= 5000:
            self.free_time += 120
        elif self.total >= 2000:
            self.free_time += 60
        if self.film:
            self.free_time += 180
        return self.free_time



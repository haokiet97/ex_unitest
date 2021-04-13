
class Color:
    color = "black"

    def __init__(self, is_holiday = False, is_sunday = False, is_saturday = False):
        self.is_holiday = is_holiday
        self.is_sunday = is_sunday
        self.is_saturday = is_saturday

    def get_color(self):
        if self.is_holiday or self.is_sunday:
            self.color = "red"
        elif self.is_saturday:
            self.color = "blue"
        return self.color

class DayColor:

    def __init__(self, is__holiday=False, is_sunday=False, is_saturday=False, is_weekday=False):
        self.is__holiday = is__holiday
        self.is_saturday = is_saturday
        self.is_weekday = is_weekday
        self.is_sunday = is_sunday

    def get_color(self):
        if self.is__holiday or self.is_sunday:
            return 'red'
        else:
            if self.is_saturday:
                return 'blue'
            else:
                return 'black'

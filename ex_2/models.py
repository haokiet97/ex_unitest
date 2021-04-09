from datetime import datetime

holiday = ["30/4","1/5","2/9"]
workday = ["Monday", "Tuesday", "Wendesday", "Thursday", "Friday"]
DEFAULT_WITH_DRAW_FEE = 110

class ATMWithdraw:
    withdraw_fee = DEFAULT_WITH_DRAW_FEE

    def __init__(self, is_vip = False, time_withdraw = datetime.now()):
        self.is_vip = is_vip
        self.time_withdraw = time_withdraw

    def get_withdraw_fee(self):
        if self.is_vip:
            self.withdraw_fee = 0
        else:
            month = self.time_withdraw.month
            day = self.time_withdraw.day
            today = "{}/{}".format(day, month)
            weekday = self.time_withdraw.strftime("%A")
            hour = self.time_withdraw.hour
            minute = self.time_withdraw.minute

            if weekday in workday and today not in holiday and self.check_free_hour(hour, minute):
                self.withdraw_fee = 0
            else:
                self.withdraw_fee = DEFAULT_WITH_DRAW_FEE

        return self.withdraw_fee

    def check_free_hour(self, hour, minute):
        if hour < 18 and hour > 8:
            return True
        elif hour == 8 and minute >= 45:
            return True
        else:
            return False


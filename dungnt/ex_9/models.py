RESULT = ["khong tim duoc phong", "tim duoc phong", "vao duoc phong", "danh bai big boss"]


class HanoiQuest:
    def __init__(self, has_magic_wand=False, has_supporter=False, has_dark_key=False, has_solar_blade=False):
        self.has_magic_wand = has_magic_wand
        self.has_supporter = has_supporter
        self.has_dark_key = has_dark_key
        self.has_solar_blade = has_solar_blade

    def check_can_defeat_big_boss(self):
        result = RESULT[0]
        if self.has_magic_wand or self.has_supporter:
            result = RESULT[1]
            if self.has_dark_key:
                result = RESULT[2]
                if self.has_solar_blade:
                    result = RESULT[3]
        return result


class BanhMi:

    def __init__(self, has_magic_wand=False, has_helper=False, has_key=False, has_sword=False):
        self.has_magic_wand = has_magic_wand
        self.has_helper = has_helper
        self.has_key = has_key
        self.has_sword = has_sword

    def let_go(self):
        if self.has_helper or self.has_magic_wand:
            if self.has_key:
                if self.has_sword:
                    return 'WINNER'
                return 'IN ROOM'
            return 'FIND ROOM'
        return "CAN'T FIND ROOM"



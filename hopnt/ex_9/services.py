from hopnt.ex_9.models import BanhMi


class BanhMiService:
    def let_go_banh_mi(self, user: BanhMi) -> int:
        return user.let_go()

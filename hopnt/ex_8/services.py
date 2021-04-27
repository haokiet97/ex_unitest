from .models import BadmintonYard


class BadmintonYardService:
    def get_fee_yard(self, user: BadmintonYard) -> int:
        return user.get_fee()

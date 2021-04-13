from .models import Banking


class BankingService:
    def get_banking_fees(self, beer: Banking) -> int:
        return beer.get_fees()

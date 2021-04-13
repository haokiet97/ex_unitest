from .models import Beer


class BeerService:
    def get_beer_amount(self, beer: Beer) -> int:
        return beer.get_amount()

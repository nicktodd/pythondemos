import random


class StockPriceRetriever:

    def get_stock_price(self):
        # this component would normally get a price from a real data feed but for now will just return a random price
            return random.random(1,100)

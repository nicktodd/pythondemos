from portfolio.StockPriceRetriever import StockPriceRetriever


class Portfolio:

    def __init__(self):
        self.stock_retriever = StockPriceRetriever()

    def calculate_portfolio_value(self):
        price = self.stock_retriever.get_stock_price()
        return price
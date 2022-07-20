from unittest.mock import MagicMock
from unittest.mock import patch
from portfolio.Portfolio import Portfolio
from portfolio.StockPriceRetriever import StockPriceRetriever
import unittest

class TestPortfolio(unittest.TestCase):

    def test_portfolio_gets_prices_from_price_retriever(self):
        # arrange
        mock_retriever = StockPriceRetriever()
        mock_retriever.get_stock_price = MagicMock(return_value = 10)
        portfolio = Portfolio()
        portfolio.stock_retriever = mock_retriever
        # act
        return_value = portfolio.calculate_portfolio_value()
        # assert
        mock_retriever.get_stock_price.assert_called_once()
        self.assertEqual(return_value, 10)
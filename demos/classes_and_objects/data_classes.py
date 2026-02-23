from dataclasses import dataclass

@dataclass(frozen=True)
class Stock:
    '''A simple data class representing a stock.'''
    symbol: str
    price: float
    volume: int

my_stock = Stock(symbol="AAPL", price=124, volume=1000)

print(my_stock)  # Output: Stock(symbol='AAPL', price=150.0

print(my_stock.__doc__)

name = "nick"
name1 = "nick"

print(name == name1)  # Output: True
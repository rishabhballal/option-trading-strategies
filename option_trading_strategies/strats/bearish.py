from .. import instruments
from .. import portfolio

stock = instruments.Stock()
put_80 = instruments.Put(stock=stock, strike=80)

covered_put = portfolio.Portfolio(
    strategy='Covered Put',
    long=[],
    short=[stock, put_80]
)

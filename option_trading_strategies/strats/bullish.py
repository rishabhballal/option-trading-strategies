from .. import instruments
from .. import portfolio

stock = instruments.Stock()
call_120 = instruments.Call(stock=stock, strike=120)

covered_call = portfolio.Portfolio(
    strategy='Covered call',
    long=[stock],
    short=[call_120]
)

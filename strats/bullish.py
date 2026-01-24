import strats.instruments
import strats.portfolio

stock = strats.instruments.Stock()
call_120 = strats.instruments.Call(stock=stock, strike=120)

covered_call = strats.portfolio.Strategy(
    title='Covered Call',
    portfolio={'buy': [stock], 'sell': [call_120]},
    max_profit='K - S_0 + C = ' + \
        str(round(call_120.strike - stock.S_0 + call_120.price())),
    max_loss=f'S_0 - C = {round(stock.S_0 - call_120.price())}',
)

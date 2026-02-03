import option_trading_strategies as ots

# predefined
ots.strats.long_iron_condor.plot_payoff()

# custom
stock = ots.Stock(S_0=200, rate=0.04, vol=0.25)
ots.Portfolio(
    strategy='Long collar',
    long=[stock, ots.Put(stock=stock, strike=180, expiry=2)],
    short=[ots.Call(stock=stock, strike=220, expiry=2)]
).plot_payoff()

import option_trading_strategies as ots

# predefined
ots.strats.long_iron_condor.plot_payoff()

# custom
ots.stock.reset(S_0=200, rate=0.04, vol=0.25)
ots.Portfolio(
    strategy='Long collar',
    long=[ots.stock, ots.put(strike=180, expiry=2)],
    short=[ots.call(strike=220, expiry=2)]
).plot_payoff()

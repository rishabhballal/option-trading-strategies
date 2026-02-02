# Option trading strategies

This simple project illustrates the standard trading strategies involving vanilla options. These strategies can be categorised according to the trader's outlook as follows.

* Bullish &ndash; an expectation that the stock price will rise.

    Includes long call, short put, covered call, protective put, bull call spread, bull put spread, long synthetic forward, long combo, bull call ladder, bear call ladder, covered short straddle, covered short strangle, call ratio backspread, call ratio spread, long collar, long bullish seagull spread, and short bullish seagull spread.

* Bearish &ndash; an expectation that the stock price will fall.

    Includes short call, long put, covered put, protective call, bear call spread, bear put spread, short synthetic forward, short combo, bull put ladder, bear put ladder, put ratio backspread, put ratio spread, short collar, long bearish seagull spread, and short bearish seagull spread.

* Volatility &ndash; an expectation that the stock price will move considerably in either direction.

    Includes long straddle, long strangle, long guts, long call synthetic straddle, long put synthetic straddle, strap, strip, short call butterfly, short put butterfly, long iron butterfly, short call condor, short put condor, and long iron condor.

* Sideways &ndash; an expectation that the stock price will remain within a small neighbourhood of itself.

    Includes short straddle, short strangle, short guts, short call synthetic straddle, short put synthetic straddle, long call butterfly, long put butterfly, short iron butterfly, long call condor, long put condor, and short iron condor.

----

Displaying the payoff diagram of any one of these predefined strategies is relatively straightforward.

```python
# main.py
import option_trading_strategies as ots

ots.strats.long_collar.plot_payoff()
```

This will also output the portfolio positions of the strategy. The parameters of the market instruments (namely, of the underlying stock and the vanilla options) have been assigned default values so that the focus is on the qualitative behaviour. The following code shows how one can tweak these values if desired.

```python
# main.py
ots.stock.reset(S_0=200, rate=0.04, vol=0.25)

ots.Portfolio(
    strategy='Long collar',
    long=[ots.stock, ots.put(strike=180, expiry=2)],
    short=[ots.call(strike=220, expiry=2)]
).plot_payoff()
```

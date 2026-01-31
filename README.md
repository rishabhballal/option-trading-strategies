# Option trading strategies

This simple project illustrates the basic trading strategies involving vanilla options. These strategies can be categorised according to the trader's outlook as follows:

* Bullish -- an expectation that the stock price will rise.

    Includes long call, short put, covered call, protective put, bull call spread, bull put spread, long synthetic forward, long combo, bull call ladder, bear call ladder, covered short straddle, covered short strangle, call ratio backspread, call ratio spread, long collar, long bullish seagull spread, and short bullish seagull spread.

* Bearish -- an expectation that the stock price will fall.

    Includes short call, long put, covered put, protective call, bear call spread, bear put spread, short synthetic forward, short combo, bull put ladder, bear put ladder, put ratio backspread, put ratio spread, short collar, long bearish seagull spread, and short bearish seagull spread.

* Volatility -- an expectation that the stock price will move considerably in either direction.

    Includes long straddle, long strangle, long guts, long call synthetic straddle, long put synthetic straddle, strap, strip, short call butterfly, short put butterfly, long iron butterfly, short call condor, short put condor, and long iron condor.

* Sideways -- an expectation that the stock price will remain within a small neighbourhood of itself.

    Includes short straddle, short strangle, short guts, short call synthetic straddle, short put synthetic straddle, long call butterfly, long put butterfly, short iron butterfly, long call condor, long put condor, and short iron condor.

----

To display the portfolio positions and payoff diagram of any strategy is relatively straightforward.

```python
# main.py
import option_trading_strategies as ots

ots.long_iron_condor.info()
```

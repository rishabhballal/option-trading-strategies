# Option trading strategies

This project is a work-in-progress. It illustrates the basic trading strategies involving vanilla options, as compiled within the article [151 Trading Strategies](https://ssrn.com/abstract=3247865). The strategies can be categorised according to the trader's outlook:

* Bullish: covered call, protective put, bull call spread, bull put spread, long synthetic forward, long combo, bull call ladder, bear call ladder, covered short straddle, covered short strangle, call ratio backspread, call ratio spread.
* Bearish: covered put, protective call, bear call spread, bear put spread, short synthetic forward, short combo, bull put ladder, bear put ladder, put ratio backspread, put ratio spread.
* Volatility: long straddle, long strangle, long guts, long call synthetic straddle, long put synthetic straddle, strap, strip.
* Sideways: short straddle, short strangle, short guts, short call synthetic straddle, short put synthetic straddle.

For example, the following code will display the portfolio and payoff diagram of the covered call strategy.

```python
# main.py
import option_trading_strategies as ots

ots.bullish.covered_call.info()
```

This can be tweaked in an obvious manner to suit the other strategies listed above.

from .. import stock, call, put
from ..portfolio import Portfolio

covered_put = Portfolio(
    strategy='Covered Put',
    long=[],
    short=[stock, put(strike=80)]
)

protective_call = Portfolio(
    strategy='Protective call',
    long=[call(strike=120)],
    short=[stock]
)

bear_call_spread = Portfolio(
    strategy='Bear call spread',
    long=[call(strike=120)],
    short=[call(strike=100)]
)

bear_put_spread = Portfolio(
    strategy='Bear put spread',
    long=[put(strike=100)],
    short=[put(strike=80)]
)

short_synthetic_forward = Portfolio(
    strategy='Short synthetic forward',
    long=[put(strike=100)],
    short=[call(strike=100)]
)

short_combo = Portfolio(
    strategy='Short combo',
    long=[put(strike=80)],
    short=[call(strike=120)]
)

bull_put_ladder = Portfolio(
    strategy='Bull put ladder',
    long=[put(strike=80), put(strike=60)],
    short=[put(strike=100)]
)

bear_put_ladder = Portfolio(
    strategy='Bear put ladder',
    long=[put(strike=100)],
    short=[put(strike=80), put(strike=60)]
)

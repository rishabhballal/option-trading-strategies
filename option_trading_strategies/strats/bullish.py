from .. import stock, call, put
from ..portfolio import Portfolio

covered_call = Portfolio(
    strategy='Covered call',
    long=[stock],
    short=[call(strike=120)]
)

protective_put = Portfolio(
    strategy='Protective put',
    long=[stock, put(strike=80)],
    short=[]
)

bull_call_spread = Portfolio(
    strategy='Bull call spread',
    long=[call(strike=100)],
    short=[call(strike=120)]
)

bull_put_spread = Portfolio(
    strategy='Bull put spread',
    long=[put(strike=80)],
    short=[put(strike=100)]
)

long_synthetic_forward = Portfolio(
    strategy='Long synthetic forward',
    long=[call(strike=100)],
    short=[put(strike=100)]
)

long_combo = Portfolio(
    strategy='Long combo',
    long=[call(strike=120)],
    short=[put(strike=80)]
)

bull_call_ladder = Portfolio(
    strategy='Bull call ladder',
    long=[call(strike=100)],
    short=[call(strike=120), call(strike=140)]
)

bear_call_ladder = Portfolio(
    strategy='Bear call ladder',
    long=[call(strike=120), call(strike=140)],
    short=[call(strike=100)]
)

covered_short_straddle = Portfolio(
    strategy='Covered short straddle',
    long=[stock],
    short=[call(strike=120), put(strike=120)]
)

covered_short_strangle = Portfolio(
    strategy='Covered short strangle',
    long=[stock],
    short=[call(strike=120), put(strike=80)]
)

from .. import stock, call, put
from ..instruments import Portfolio

long_call = Portfolio(
    strategy='Long call',
    long=[call(strike=120)],
    short=[]
)

short_put = Portfolio(
    strategy='Short put',
    long=[],
    short=[put(strike=80)]
)

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

call_ratio_backspread = Portfolio(
    strategy='Call ratio backspread',
    long=[call(strike=110), call(strike=110)],
    short=[call(strike=90)]
)

call_ratio_spread = Portfolio(
    strategy='Call ratio spread',
    long=[call(strike=90)],
    short=[call(strike=110), call(strike=110)]
)

long_collar = Portfolio(
    strategy='Long collar',
    long=[stock, put(strike=80)],
    short=[call(strike=120)]
)

long_bullish_seagull_spread = Portfolio(
    strategy='Long bullish seagull spread',
    long=[call(strike=130), put(strike=80)],
    short=[put(strike=100)]
)

short_bullish_seagull_spread = Portfolio(
    strategy='Short bullish seagull spread',
    long=[call(strike=100)],
    short=[call(strike=120), put(strike=80)]
)

from .. import stock, call, put
from ..portfolio import Portfolio

long_straddle = Portfolio(
    strategy='Long straddle',
    long=[call(strike=100), put(strike=100)],
    short=[]
)

long_strangle = Portfolio(
    strategy='Long strangle',
    long=[call(strike=120), put(strike=80)],
    short=[]
)

long_guts = Portfolio(
    strategy='Long guts',
    long=[call(strike=80), put(strike=120)],
    short=[]
)

long_call_synthetic_straddle = Portfolio(
    strategy='Long call synthetic straddle',
    long=[call(strike=100), call(strike=100)],
    short=[stock]
)

long_put_synthetic_straddle = Portfolio(
    strategy='Long put synthetic straddle',
    long=[stock, put(strike=100), put(strike=100)],
    short=[]
)

strap = Portfolio(
    strategy='Strap',
    long=[call(strike=100), call(strike=100), put(strike=100)],
    short=[]
)

strip = Portfolio(
    strategy='Strip',
    long=[call(strike=100), put(strike=100), put(strike=100)],
    short=[]
)

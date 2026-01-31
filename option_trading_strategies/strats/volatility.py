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

short_call_butterfly = Portfolio(
    strategy='Short call butterfly',
    long=[call(strike=100), call(strike=100)],
    short=[call(strike=120), call(strike=80)]
)

short_put_butterfly = Portfolio(
    strategy='Short put butterfly',
    long=[put(strike=100), put(strike=100)],
    short=[put(strike=80), put(strike=120)]
)

long_iron_butterfly = Portfolio(
    strategy='Long iron butterfly',
    long=[put(strike=100), call(strike=100)],
    short=[put(strike=80), call(strike=120)]
)

short_call_condor = Portfolio(
    strategy='Short call condor',
    long=[call(strike=90), call(strike=110)],
    short=[call(strike=70), call(strike=130)]
)

short_put_condor = Portfolio(
    strategy='Short put condor',
    long=[put(strike=90), put(strike=110)],
    short=[put(strike=70), put(strike=130)]
)

long_iron_condor = Portfolio(
    strategy='Long iron condor',
    long=[put(strike=90), call(strike=110)],
    short=[put(strike=70), call(strike=130)]
)

from .. import stock, call, put
from ..portfolio import Portfolio

short_straddle = Portfolio(
    strategy='Short straddle',
    long=[],
    short=[call(strike=100), put(strike=100)]
)

short_strangle = Portfolio(
    strategy='Short strangle',
    long=[],
    short=[call(strike=120), put(strike=80)]
)

short_guts = Portfolio(
    strategy='Short guts',
    long=[],
    short=[call(strike=80), put(strike=120)]
)

short_call_synthetic_straddle = Portfolio(
    strategy='Short call synthetic straddle',
    long=[stock],
    short=[call(strike=100), call(strike=100)]
)

short_put_synthetic_straddle = Portfolio(
    strategy='Short put synthetic straddle',
    long=[],
    short=[stock, put(strike=100), put(strike=100)]
)

long_call_butterfly = Portfolio(
    strategy='Long call butterfly',
    long=[call(strike=120), call(strike=80)],
    short=[call(strike=100), call(strike=100)]
)

long_put_butterfly = Portfolio(
    strategy='Long put butterfly',
    long=[put(strike=80), put(strike=120)],
    short=[put(strike=100), put(strike=100)]
)

short_iron_butterfly = Portfolio(
    strategy='Short iron butterfly',
    long=[put(strike=80), call(strike=120)],
    short=[put(strike=100), call(strike=100)]
)

long_call_condor = Portfolio(
    strategy='Long call condor',
    long=[call(strike=70), call(strike=130)],
    short=[call(strike=90), call(strike=110)]
)

long_put_condor = Portfolio(
    strategy='Long put condor',
    long=[put(strike=70), put(strike=130)],
    short=[put(strike=90), put(strike=110)]
)

short_iron_condor = Portfolio(
    strategy='Short iron condor',
    long=[put(strike=70), call(strike=130)],
    short=[put(strike=90), call(strike=110)]
)

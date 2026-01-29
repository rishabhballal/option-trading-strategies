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

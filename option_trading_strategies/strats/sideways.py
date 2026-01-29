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

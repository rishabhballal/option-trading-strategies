from . import instruments

stock = instruments.Stock(S_0=100, rate=0.05, vol=0.40)

def call(strike=120, expiry=1):
    return instruments.Call(stock=stock, strike=strike, expiry=expiry)

def put(strike=80, expiry=1):
    return instruments.Put(stock=stock, strike=strike, expiry=expiry)

from .strats.bullish import *
from .strats.bearish import *
from .strats.volatility import *
from .strats.sideways import *

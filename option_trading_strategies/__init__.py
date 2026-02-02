from .instruments import *

stock = Stock(S_0=100, rate=0.05, vol=0.40)

def call(strike=120, expiry=1):
    return Call(stock=stock, strike=strike, expiry=expiry)

def put(strike=80, expiry=1):
    return Put(stock=stock, strike=strike, expiry=expiry)

from . import strats

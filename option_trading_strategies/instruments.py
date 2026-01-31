import math
from scipy.stats import norm

class Stock:
    def __init__(self, S_0, rate, vol):
        self.S_0 = S_0
        self.rate = rate
        self.vol = vol

    def payoff(self, S_T):
        return S_T - self.S_0

class Call:
    def __init__(self, stock, strike, expiry):
        self.stock = stock
        self.strike = strike
        self.expiry = expiry

    def price(self):
        d_minus = 1 / (self.stock.vol * math.sqrt(self.expiry)) * \
            (math.log(self.stock.S_0 / self.strike) + \
                (self.stock.rate - 0.5 * self.stock.vol**2) * self.expiry)
        d_plus = d_minus + self.stock.vol * math.sqrt(self.expiry)
        return self.stock.S_0 * norm.cdf(d_plus) - self.strike * \
            math.exp(-self.stock.rate * self.expiry) * norm.cdf(d_minus)

    def payoff(self, S_T):
        return max(S_T - self.strike, 0) - self.price()

class Put:
    def __init__(self, stock, strike, expiry):
        self.stock = stock
        self.strike = strike
        self.expiry = expiry

    def price(self):
        d_minus = 1 / (self.stock.vol * math.sqrt(self.expiry)) * \
            (math.log(self.stock.S_0 / self.strike) + \
                (self.stock.rate - 0.5 * self.stock.vol**2) * self.expiry)
        d_plus = d_minus + self.stock.vol * math.sqrt(self.expiry)
        return -self.stock.S_0 * norm.cdf(-d_plus) + self.strike * \
            math.exp(-self.stock.rate * self.expiry) * norm.cdf(-d_minus)

    def payoff(self, S_T):
        return max(self.strike - S_T, 0) - self.price()

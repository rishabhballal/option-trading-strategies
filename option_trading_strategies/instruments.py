import math
from scipy.stats import norm
import matplotlib.pyplot as plt

class Stock:
    def __init__(self, S_0, rate, vol):
        self.S_0 = S_0
        self.rate = rate
        self.vol = vol

    def payoff(self, S_T):
        return S_T - self.S_0

    def reset(self, S_0, rate, vol):
        self.S_0 = S_0
        self.rate = rate
        self.vol = vol

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

class Portfolio:
    def __init__(self, strategy, long, short):
        self.strategy = strategy
        self.position = {'Long': long, 'Short': short}

    def payoff(self, S_T):
        return sum([x.payoff(S_T) for x in self.position['Long']]) - \
            sum([x.payoff(S_T) for x in self.position['Short']])

    def plot_payoff(self):
        pf = {'Long': [], 'Short': []}
        for k in self.position.keys():
            for x in self.position[k]:
                if x.__class__.__name__ == 'Stock':
                    pf[k].append(x.__class__.__name__)
                    S_0 = x.S_0
                else:
                    pf[k].append(f'{x.__class__.__name__} struck at {x.strike}')
                    S_0 = x.stock.S_0
        S_T = range(max(S_0 - 100, 0), S_0 + 101)
        P_T = [self.payoff(x) for x in S_T]
        plt.figure(figsize=(8, 6))
        plt.plot(S_T, P_T)
        plt.plot(S_T, [0] * len(S_T), color='black')
        plt.xlabel('Final stock price')
        plt.ylabel('Payoff')
        plt.title(self.strategy)
        plt.subplots_adjust(bottom=0.2)
        plt.figtext(
            0.125, 0.05,
            f'Initial stock price = {S_0}\n' +
            f'Long: [{', '.join(pf['Long'])}], ' +
            f'Short: [{', '.join(pf['Short'])}]',
            ha='left')
        plt.grid()
        plt.show()

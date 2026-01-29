import matplotlib.pyplot as plt

class Portfolio:
    def __init__(self, strategy, long, short):
        self.strategy = strategy
        self.position = {'Long': long, 'Short': short}

    def _payoff(self, S_T):
        return sum([x.payoff(S_T) for x in self.position['Long']]) - \
            sum([x.payoff(S_T) for x in self.position['Short']])

    def info(self):
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
        P_T = [self._payoff(x) for x in S_T]
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

import copy
import matplotlib.pyplot as plt

class Portfolio:
    def __init__(self, strategy, long, short):
        self.strategy = strategy
        self.position = {'Long': long, 'Short': short}

    def _payoff(self, S_T):
        return sum([x.payoff(S_T) for x in self.position['Long']]) - \
            sum([x.payoff(S_T) for x in self.position['Short']])

    def details(self, S_T=range(201)):
        print(f'Strategy:\t{self.strategy}')

        pf = {'Long': [], 'Short': []}
        for k in self.position.keys():
            for x in self.position[k]:
                if x.__class__.__name__ == 'Stock':
                    pf[k].append(x.__class__.__name__)
                else:
                    pf[k].append(f'{x.__class__.__name__} struck at {x.strike}')
        print(f'Portfolio:\t{pf}')

        P_T = [self._payoff(x) for x in S_T]
        print(f'If the final stock price is between {min(S_T)} and {max(S_T)}:')
        print(f'Max profit = {round(max(P_T))}', end='\t\t')
        print(f'Max loss = {-round(min(P_T))}')

        plt.plot(S_T, P_T)
        plt.plot(S_T, [0] * len(S_T), color='black')
        plt.xlabel('Final stock price')
        plt.ylabel('Payoff')
        plt.title(self.strategy)
        plt.grid()
        plt.show()

class Strategy:
    def __init__(self, title, portfolio, max_profit, max_loss):
        self.title = title
        self.portfolio = portfolio
        self.max_profit = max_profit
        self.max_loss = max_loss

    def description(self):
        pf = {'Buy': [], 'Sell': []}
        for key in self.portfolio.keys():
            for x in self.portfolio[key]:
                if x.__class__.__name__ == 'Stock':
                    pf[key].append(x.__class__.__name__)
                else:
                    pf[key].append(f'{x.__class__.__name__} struck at {x.strike}')
        print(f'Strategy: {self.title}')
        print(f'Portfolio: {pf}')
        print(f'Max profit = {self.max_profit}')
        print(f'Max loss = {self.max_loss}')

    def payoff(self, S_T):
        return sum([x.payoff(S_T) for x in self.portfolio['Buy']]) - \
            sum([x.payoff(S_T) for x in self.portfolio['Sell']])

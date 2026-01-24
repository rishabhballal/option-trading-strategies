import matplotlib.pyplot as plt
import strats.bullish as bull

strat = bull.covered_call

strat.description()

S_T = range(50, 151)
plt.plot(S_T, [strat.payoff(x) for x in S_T])
plt.plot(S_T, [0] * len(S_T), color='black')
plt.xlabel('Final stock price')
plt.ylabel('Payoff')
plt.title(strat.title)
plt.grid()
plt.show()

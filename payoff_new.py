def payoff_longcall(S, K, c):
    """
    Calculate the payoff of a long call option and the net profit
    """
    profit = np.where(S<=K, 0, S-K)
    net_profit= profit - c
    return net_profit

def payoff_longput (S, K, p):
    """
    Calculate the payoff of the long put option and the net profit
    """   
    profit = np.where(S>=K, 0, K-S)
    net_profit= profit - p
    return net_profit

def payoff_bull_call_spread(S, K1, K2, c, v):
    """
    Calculate the payoff and net profit of a bull call spread operation. 
    K1: Lower Strike Price (call option purchased)
    K2: Higher Strike Price (call option issued/sold)
    The spread for the higher strike price call issued is stablished $10 superior than the call option with lower strike price
    """
    profitshort= np.where(S<=K1, 0, S-K1)
    profitlong= np.where(S<=K2, 0, S-K2)
    netprofitshort= profitshort - c
    netprofitlong= profitlong - v
    results_bcs= netprofitshort - netprofitlong
    return results_bcs

def payoff_straddle(S, K1, K2, c, p):
    """
    Calculate the payoff and net profit of a Straddle Operation.
    K1: strike price of the put option
    K2: strike price of the call option
    """
    profitput = np.where(S>=K1, 0, K1-S)
    profitcall = np.where(S<=K2, 0, S-K2)
    netprofit_call = profitcall - c
    netprofit_put = profitput - p
    result_straddle = netprofit_call + netprofit_put
    return result_straddle



import numpy as np
secuencia = np.linspace(0, 200, 20)

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Long Call

results_call =payoff_longcall (secuencia, 100, 5)
print(results_call)

axes[0,0].set_xlabel("Stock Price")
axes[0,0].set_ylabel("Net Profit")
axes[0, 0].plot(secuencia, results_call)     
axes[0, 0].axhline(0)
axes[0, 0].axvline(105)             
axes[0, 0].set_title("Long Call")

# Long Put

results_put =payoff_longput (secuencia, 100, 5)
print(results_put)

axes[0,1].set_xlabel("Stock Price")
axes[0,1].set_ylabel("Net Profit")
axes[0, 1].plot(secuencia, results_put)
axes[0, 1].axhline(0)
axes[0, 1].axvline(95)
axes[0, 1].set_title("Long Put")
 
# Bull Call Spread

results_bcs = payoff_bull_call_spread(secuencia, 100, 110, 7, 5)
print(results_bcs)

axes[1,0].set_xlabel("Stock Price")
axes[1,0].set_ylabel("Net Profit")
axes[1, 0].plot(secuencia, results_bcs)
axes[1, 0].axhline(0)
axes[1, 0].axvline(102)
axes[1, 0].set_title("Bull Call Spread")


# Straddle

results_straddle = payoff_straddle(secuencia, 100, 100, 5, 5)
print(results_straddle)

axes[1,1].set_xlabel("Stock Price")
axes[1,1].set_ylabel("Net Profit")
axes[1, 1].plot(secuencia, results_straddle)
axes[1, 1].axhline(0)
axes[1, 1].axvline(90)              
axes[1, 1].axvline(110)
axes[1, 1].set_title("Straddle")

plt.tight_layout()
plt.show()


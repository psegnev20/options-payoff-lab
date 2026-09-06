def payoff_call(S,K):
    '''
    Calculates the payoff of a call option.
    '''
    return max(S-K,0)
  

def payoff_put(S,K):
    '''
    Calculates the payoff of a put option.
    '''
    return max(K-S,0)

assert payoff_call(110, 100) == 10
assert payoff_put(90, 100) == 10
print("Tests OK")

#For a call option, the payoff is positive if the stock price S is greater than the strike price K.
#For a put option, the payoff is positive if the stock price S is less than the strike price K.
#The code belowe is a simple implementation of the payoff functions for call and put options. It uses the max function to ensure that the payoff is never negative, as options cannot have a negative payoff.
'''
if S > K: 
       print("The operation is ITM")
    elif S == K:
        print("The operation is ATM")
    else: 
        print("The operation is OTM")
  if S < K: 
        print("The operation is ITM")
    elif S == K:
        print("The operation is ATM")
    else: 
        print("The operation is OTM")
'''


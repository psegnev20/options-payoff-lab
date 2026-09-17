from payoff_new import payoff_longcall   # ajusta el nombre del import a tu archivo

def test_longcall_breakeven():
    resultado = payoff_longcall(105, 100, 5)   # S = tu breakeven, K, c
    assert abs(resultado) < 0.01


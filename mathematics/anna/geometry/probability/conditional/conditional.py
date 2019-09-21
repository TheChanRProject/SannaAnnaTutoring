import numpy as np
def C(n ,r):
    return np.math.factorial(n) / (np.math.factorial(n) - np.math.factorial(r))


prob_num = 4 * 3 * 2 * 4 * 3
prob_denom = 52 * 51 * 50 * 49 * 48

prob_num / prob_denom

(C(4,3) * C(4, 2)) / C(52,5)

(C(4,3) + C(4,2)) / C(52,5)

(C(9,3) * C(10,2)) / C(52,5)

P_nVDP = (5000 - 3) / 5000
P_nADP = (1000 - 2) / 1000

P_nADP * P_nVDP

C(49, 6) / np.math.factorial(49 )

C(49, 6)

1 / C(49, 6)

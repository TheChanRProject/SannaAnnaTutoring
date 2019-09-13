import numpy as np

V_c = np.pi*(6**2)*28

n_marbles = V_c / (36*np.pi)
n_marbles

V_box = 18 * 24 * 12
V_trail = 4 * 3 * 3
V_box
V_trail
n_trail = V_box / V_trail

n_trail

V_g_machine = (4/3)*np.pi*(6**3)
V_gumball = (4/3)*np.pi*(0.6**3)
n_gumballs = V_g_machine / V_gumball
n_gumballs

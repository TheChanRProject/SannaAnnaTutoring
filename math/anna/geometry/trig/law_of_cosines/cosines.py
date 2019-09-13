import numpy as np
def law_of_cosines(a,b, angle):
    return a**2 + b**2 + 2*a*b*np.cos(np.deg2rad(angle))

print(law_of_cosines(9, 5, 120))

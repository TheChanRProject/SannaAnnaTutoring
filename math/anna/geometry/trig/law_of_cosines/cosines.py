import numpy as np
def law_of_cosines(a,b, angle):
    return np.sqrt(a**2 + b**2 - 2*a*b*np.cos(np.deg2rad(angle)))

def side_squared(a,b,angle):
    return a**2 + b**2 - 2*a*b*np.cos(np.deg2rad(angle))

print(law_of_cosines(9, 5, 120))
print(law_of_cosines(4, 7, 20))
print(side_squared(9,5,120))
np.sqrt(16 + 49 + 2*(4*7*np.cos(np.deg2rad(20))))

16 + (3.5)**2
360 - 2*36
288 / 2
144 / 2
180 - (72 + 18)
print(law_of_cosines(40, 70, 144))

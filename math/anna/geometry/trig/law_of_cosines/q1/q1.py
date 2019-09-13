import numpy as np

def law_of_cosines(a,b, angle):
    return np.sqrt((a**2 + b**2 + 2*a*b*np.cos(np.deg2rad(angle))))

print(law_of_cosines(16, 11, 33))

16 * 11
2 * 172

144 + 225
360 / 2
369 - 180
np.sqrt(189)

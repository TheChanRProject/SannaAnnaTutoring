144 + 16**2
import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)
np.sqrt(400)


# Question 28
X = [-2, -5, 2, -2]
Y = [3, -4, -1, 3]
plt.figure(figsize=(10,10))
plt.plot(X,Y, 'g-')

X = [2, 8, 8, 2]
Y = [5, 5, 3, 3]

def distance(a, b):
    return np.sqrt(np.power(b[0] - a[0], 2) + np.power(b[1] - a[1], 2))

d1 = distance((2,5) , (8,5))
d2 = distance((8,5), (8,3))
d3 = distance((8,3), (2,3))
d4 = distance((2,5), (2,3))

print(sum([d1, d2, d3 ,d4]))

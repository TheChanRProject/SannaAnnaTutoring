import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)
from itertools import combinations
X = [3, 5, 5, 3, 3]
Y = [9, 9, 3, 3, 9]

def midpoint(X, Y):
    return ((X[0] + X[1]) / 2, (Y[0] + Y[1]) / 2)


points = list(zip(X, Y))

poss = set(combinations(points, 2))
print(poss)
poss = [i for i in poss if i[0] != i[1]]
print(poss)
poss = poss[0:4]
poss
mid_points = [midpoint(i[0][0], i[0][1]) for i in poss]
print(mid_points)
plt.figure(figsize=(10,10))
plt.plot(X, Y, 'g')
plt.title("Rectangular Garden", size=18)
plt.text(4, 3.2, '2', fontsize=12)
plt.text(4, 8.8, '2', fontsize=12)
plt.text(3.1, 6, '6', fontsize=12)
plt.text(4.8, 6, '6', fontsize=12)

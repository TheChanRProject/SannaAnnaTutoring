def q36_circle(x, y, r):
    circle = (x - 3)**2 + y**2
    if circle < r**2:
        print("Interior")
    elif circle == r**2:
        print("On the circle")
    elif circle > r**2:
        print("Exterior")
    return circle

A = (-1, 1)
B = (10, 0)
C = (4, -8)

q36_circle(A[0], A[1], 7)
q36_circle(B[0], B[1], 7)
q36_circle(C[0], C[1], 7)

import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)

X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(X,Y)
F = (X - 3)**2 + (Y)**2 - 49
plt.figure(figsize=(10,10))
plt.contour(X,Y,F,[0], colors=['purple'])
x,y = np.array([[-1, 1], [10, 0], [4, -8]]).T
plt.scatter(x,y, color="blue")
plt.title(r"Graph of $(x-3)^2 + y^2 = 49$", size=24, color="silver")
plt.savefig("math/anna/geometry/coordinate_geometry/quiz2/q36/circle.png")

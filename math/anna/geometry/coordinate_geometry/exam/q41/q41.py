import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai")
A = [-1, -1, 4]
B = [1, 6, -8]
plt.figure(figsize=(10,10))
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x,y)
F = (X+1)**2 + Y**2 - 36
plt.contour(X, Y, F, [0], colors=['green'])
plt.gca().set_aspect('equal')
plt.plot(A, B, 'ro')
plt.savefig("math/anna/geometry/coordinate_geometry/exam/q41/circle.png")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=False)
plt.figure(figsize=(10,10))
A = [-1, -2, 4]
B = [1, 1, -8]
x = np.linspace(-8,8, 100)
y = np.linspace(-8,8, 100)
X,Y = np.meshgrid(x,y)
F = X**2 + Y**2 - 5
plt.contour(X, Y, F, [0], colors=['blue'])
plt.plot(A,B, 'go')
plt.gca().set_aspect('equal')
plt.savefig("math/anna/geometry/coordinate_geometry/exam/q43/circle.png")
plt.show()

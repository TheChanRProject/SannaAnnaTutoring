import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)

X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(X,Y)
F = (X - 3)**2 + (Y)**2 - 49
plt.figure(figsize=(10,10))
plt.contour(X,Y,F,[0], colors=['green'])
x,y = np.array([[-1, 1], [10, 0], [4, -8]]).T
plt.scatter(x,y, color="red")
plt.title(r"Graph of $(x-3)^2 + y^2 = 49$", size=24, color="silver")
plt.savefig("math/anna/geometry/coordinate_geometry/circles/q5/graph.png")

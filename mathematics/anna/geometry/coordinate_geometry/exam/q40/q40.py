import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=False)
def midpoint(X, Y):
    return ((X[0] + X[1]) / 2, (Y[0] + Y[1]) / 2)

print(midpoint((3,0), (-4,0)))

def distance(X, Y):
    return np.sqrt((Y[0] - X[0])**2 + (Y[1] - X[1])**2)

print(distance((3,0), (-4,0)))

radius = 7 / 2

plt.figure(figsize=(10,10))
plt.axes()
circ = Circle((1.5, -2.0), radius=radius, fc='g')
plt.gca().add_patch(circ)
plt.axis("scaled")
plt.savefig("math/anna/geometry/coordinate_geometry/exam/q40/circle.png")
plt.show()

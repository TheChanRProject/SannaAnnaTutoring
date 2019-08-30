import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=False)

plt.figure(figsize=(10,10))
plt.axes()
circ = Circle((0, -1), 3.5, fc='g')
plt.gca().add_patch(circ)
plt.axis("scaled")
plt.savefig("math/anna/geometry/coordinate_geometry/exam/q42/circle.png")
plt.show()

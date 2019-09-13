import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=False)
plt.figure(figsize=(10,10))
plt.axes()
circle = Circle((3, (-7/2)), radius=7/2, fc='b')
plt.gca().add_patch(circle)
plt.axis('scaled')
plt.savefig("math/anna/geometry/coordinate_geometry/quiz2/q35/circle.png")
plt.show()

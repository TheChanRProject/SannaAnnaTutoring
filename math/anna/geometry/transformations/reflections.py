import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=False)
x1 = [3, -4, -3, 3]
y1 = [2, 1, -2, 2]
x2 = [-3, 4, 3, -3]
y2 = [-2, -1, 2, -2]
plt.figure(figsize=(10,10))
plt.plot(x1,y1, 'g-')
plt.plot(x2, y2, 'b-')
plt.savefig("math/anna/geometry/transformations/reflection_q15.png")
plt.show()

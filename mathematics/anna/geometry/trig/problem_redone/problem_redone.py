import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=False)

X = [0, 185, 185/2, 0]
Y = [0, 0, 283, 0]
plt.figure(figsize=(10,10))
plt.plot(X,Y, 'g-')
plt.text(185/2, 1, '185')
plt.text(140, 283/2, '283')
plt.text(170,3, r'$80^{\circ}$')
plt.savefig("mathematics/anna/geometry/trig/problem_redone/triangle.png")

ab = 185 * 283

A = ab * np.sin(np.deg2rad(80))
12 * round(A / 36)

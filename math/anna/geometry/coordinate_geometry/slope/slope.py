import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)

X = [1, 3, 6, 1]
Y = [3, 5, 2, 3]

plt.figure(figsize=(10,10))
plt.plot(X,Y, 'b-')
plt.text(3,5, "Q", color="silver", size=14)
plt.text(0.9, 3, "P", color="silver", size=14)
plt.text(6,2, "R", color="silver", size=14)
plt.axhline(3, 0.05, 0.75, linewidth=2, color='g')
plt.savefig("math/anna/geometry/coordinate_geometry/slope/q22.png")

import numpy as np
import matplotlib.pyplot as plt
from os import getcwd, chdir
chdir("math/anna/geometry/coordinate_geometry/slope/q16")
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)


X = [0, 3, 5, 0]
Y = [1, 2, -4, 1]
plt.figure(figsize=(10,10))
plt.plot(X,Y, 'r-')
plt.text(0, 1, 'P', color="silver", size=14)
plt.text(3, 2, 'Q', color="silver", size=14)
plt.text(5, -4, 'R', color="silver", size=14)
plt.savefig(f"{getcwd()}/polygon.png")

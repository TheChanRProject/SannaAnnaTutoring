import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai")
X = [-1, 1, 7, 2, -1]
Y = [5, 8, -2, 0, 5]
plt.figure(figsize=(10,10))
plt.plot(X,Y, 'w-')
plt.text(-1,5, "R", color="gold", size=14)
plt.text(1, 8, "S", color="gold", size=14)
plt.text(7, -2, "T", color="gold", size=14)
plt.text(2, 0, "U", color="gold", size=14)
path = "math/anna/geometry/coordinate_geometry/slope"
plt.savefig(f"{path}/line_eq_q10.png")

X = [-1, 3, 5, -1]
Y = [1, 5, -5, 1]
plt.figure(figsize=(10,10))
plt.plot(X,Y, 'r-')
plt.text(-1, 1, "P", color="silver", size=14)
plt.text(3,5, "Q", color="silver", size=14)
plt.text(5, -5, "R", color="silver", size=14)
plt.savefig(f"{path}/line_eq_q11.png")

X = [-3, 3, 3, -3, -3]
Y = [3, 3, -3, -3, 3]
plt.figure(figsize=(10,10))
plt.plot(X,Y, 'g-')
plt.text(-3, 3, "A", color="silver", size=14)
plt.text(3, 3, "B", color="silver", size=14)
plt.text(3, -3, "C", color="silver", size=14)
plt.text(-3, -3, "D", color="silver", size=14)
plt.savefig(f"{path}/line_eq_q12.png")

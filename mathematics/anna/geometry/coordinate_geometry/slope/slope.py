import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)

X = [1, 3, 6, 1]
Y = [3, 5, 2, 3]

path = "math/anna/geometry/coordinate_geometry/slope"

plt.figure(figsize=(10,10))
plt.plot(X,Y, 'b-')
plt.text(3,5, "Q", color="silver", size=14)
plt.text(0.9, 3, "P", color="silver", size=14)
plt.text(6,2, "R", color="silver", size=14)
plt.axhline(3, 0.05, 0.75, linewidth=2, color='g')
plt.savefig("math/anna/geometry/coordinate_geometry/slope/q22.png")


# Rectangle
X = [0, 6, 5, -1, 0]
Y = [0, 3, 5, 2, 0]
plt.figure(figsize=(10,10))
plt.plot(X, Y, 'o-')
plt.text(0, 0, "R", color="silver", size=14)
plt.text(6,3, "S", color="silver", size=14)
plt.text(5, 5, "T", color="silver", size=14)
plt.text(-1, 2, "U", color="silver", size=14)
plt.savefig(f"{path}/q8.png")

X = [1, 4, 2, -4, 1]
Y = [-3, -1, 2, -2, -3]
plt.figure(figsize=(10,10))
plt.plot(X, Y, 'g-')
plt.text(1, -3, "R", color="silver", size=14)
plt.text(4, -1, "S", color="silver", size=14)
plt.text(2, 2, "T", color="silver", size=14)
plt.text(-4, -2, "U", color="silver", size=14)
plt.savefig(f"{path}/q9.png")
X = [-1, 8, 5, -4, -1]
Y = [-5, 2, 5, -2, -5]
plt.figure(figsize=(10,10))
plt.plot(X,Y, 'r-')
plt.text(-1, -5, 'R', size=14)
plt.text(8, 2, "S", size=14)
plt.text(5, 5, "T", size=14)
plt.text(-4, -2, "U", size=14)
plt.savefig(f"{path}/q10.png")

X = [2, -1, -2, 2]
Y = [2, 3, -1, 2]
plt.figure(figsize=(10,10))
plt.plot(X, Y, 'g-')
plt.text(X[0], Y[0], 'J', color="silver", size=14)
plt.text(X[1], Y[1], "K", color="silver", size=14)
plt.text(X[2], Y[2], "L", color="silver", size=14)
# plt.text(X[3], Y[3], "U", color="silver", size=14)
plt.savefig(f"{path}/q15.png")

import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)
X = [-4, -1, 0, -5, -4]
Y = [-1, -1, -5, -5, -1]

X = np.array(X)
Y = np.array(Y)

image_X = -2*X
image_Y = -2*Y

plt.figure(figsize=(20,15))
plt.plot(X, Y, '-g')
plt.text(-4, -1, 'A', size=14)
plt.text(-1, -1, 'B', size=14)
plt.text(0, -5, 'C', size=14)
plt.text(-5, -5, 'D', size=14)
plt.plot(image_X, image_Y, '-b')
plt.text(image_X[0], image_Y[0], "A' ", size=14)
plt.text(image_X[1], image_Y[1], "B' ", size=14)
plt.text(image_X[2], image_Y[2], "C' ", size=14)
plt.text(image_X[3], image_Y[3], "D' ", size=14)
plt.savefig("math/anna/geometry/transformations/q20.png")

import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)
X = np.array([0,2, -2, 0])
Y = np.array([4, -2, -2, 4])

image_X = 0.5 * X
image_Y = 0.5 * Y


plt.figure(figsize=(20,15))
plt.plot(X,Y, "r-")
plt.text(X[0], Y[0], "A", size=14)
plt.text(X[1], Y[1], "B", size=14)
plt.text(X[2], Y[2], 'C', size=14)
plt.plot(image_X, image_Y, "b-")
plt.text(image_X[0], image_Y[0], "A'", size=14)
plt.text(image_X[1], image_Y[1], "B' ", size=14)
plt.text(image_X[2], image_Y[2], "C' ", size=14)
plt.savefig("math/anna/geometry/transformations/q37.png")

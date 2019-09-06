import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)
pre_image_x = [-2, 1, 1, -2]
pre_image_y = [2, 2, -1, 2]

image_x = [-5, 2.5, 2.5, -5]
image_y = [5, 5, -2.5, 5]

line_x = np.linspace(-6, 3)
line_y =
plt.figure(figsize=(20,15))
plt.plot(pre_image_x, pre_image_y, 'b-')
plt.text(-2, 2, "A (-2, 2)", size=14)
plt.text(1, 2, "B (1,2)", size=14)
plt.text(1, -1, "C (1, -1)", size=14)
plt.plot(image_x, image_y, 'g-')
plt.text(-5, 5, "A' (-5, 5)", size=14)
plt.text(2.5, 5, r"B' ($\frac{5}{2}$, 5)", size=14)
plt.text(2.5, -2.5, r"C' ($\frac{5}{2}$, $-\frac{5}{2}$)", size=14)

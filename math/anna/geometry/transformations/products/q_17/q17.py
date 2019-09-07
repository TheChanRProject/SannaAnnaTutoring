import numpy as np
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)

EFGH_x = np.array([-6, -6, -2, -2, -6])
EFGH_y = np.array([-1, 3, 3, -1, -1])

t1_x = (2/3)*final_x
t1_y = (2/3)*final_y

final_x = np.array([-9, -9, -3, -3, -9])
final_y = np.array([-12, -6, -6, -12, -12])

plt.figure(figsize=(20,15))
plt.plot(EFGH_x, EFGH_y, "r-")
plt.plot(t1_x, t1_y , "b-")
plt.plot(final_x, final_y, "g-")

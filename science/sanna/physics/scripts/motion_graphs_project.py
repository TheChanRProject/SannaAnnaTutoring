import numpy as np
import pandas as pd

x = np.array([float(i) for i in range(0,11)])
print(x)

y = np.array([0.00, 2.25, 4.38, 6.30, 8.30, 10.26, 12.30, 14.22, 16.43, 18.35, 20.00])
print(y)

import matplotlib.pyplot as plt
plt.title("Motion Graph")
plt.xlabel("Distance (meters)")
plt.ylabel("Time (seconds)")
plt.plot(x,y, 'b-', marker='o')
plt.savefig('motion-graph.jpeg')

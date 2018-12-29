import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

xVals = np.arange(-10,10    ,0.1)

def polynomial1(x):
    return pow(3*x,2) + 4*x + 2

yVals = polynomial1(xVals)

plt.plot(xVals, yVals)
plt.title("Sample Quadratic Function")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

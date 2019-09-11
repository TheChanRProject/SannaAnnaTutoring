import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme="monokai", grid=True)

X = [-6, -6, -2, -2, -6]
Y = [-5, -2, -2, -5, -5]

DEFG = zip(X, Y)
DEFG = list(DEFG)

DEFG

tDEFG = [(i[0], i[1] + 3) for i in DEFG]
tDEFG

tX = [i[0] for i in tDEFG]
tY = [i[1] for i in tDEFG]

rDEFG = [(-1*i[1], i[0]) for i in tDEFG]
rDEFG

rX = [i[0] for i in rDEFG]
rY = [i[1] for i in rDEFG]

plt.figure(figsize=(20,15))
plt.plot(X,Y, 'g-')
plt.plot(tX, tY, 'r-')
plt.plot(rX, rY, 'b-')
plt.savefig("math/anna/geometry/transformations/exam/exam.png")

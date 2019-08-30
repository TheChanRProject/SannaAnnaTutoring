import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def midpoint(X, Y):
    return ((X[0] + X[1]) / 2, (Y[0] + Y[1]) / 2)

print(midpoint((3,0), (-4,0)))

def distance(X, Y):
    return np.sqrt((Y[0] - X[0])**2 + (Y[1] - X[1])**2)

print(distance((3,0), (-4,0)))

radius = 7 / 2

import numpy as np
from itertools import combinations
X = [-7, -5, -3, -5, -7]
X2 = [-9, -7, -5, -7, -9]

Y = [4, 7, 4, 1, 4]
Y2 = [0, 3, 0, -3, 0]

def distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

points = list(zip(X, Y))
points

point_distances = [distance(points[0], points[1]), distance(points[0], points[2]), distance(points[0], points[3])]

point_distances

prime_points = list(zip(X2, Y2))

prime_distances = [distance(prime_points[0], prime_points[1]), distance(prime_points[0], prime_points[2]), distance(prime_points[0], prime_points[3])]
prime_distances

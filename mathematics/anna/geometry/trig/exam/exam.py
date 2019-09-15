import numpy as np
from mathematics.anna.geometry.trig.law_of_cosines.law_of_cosines import Cosine

angle_A = np.rad2deg(np.arcsin(((7*np.sin(np.deg2rad(95))) / 9)))
angle_A

# Problem 7
b = (18 * np.sin(np.deg2rad(20))) / np.sin(np.deg2rad(130))
b

# Problem 9
side = Cosine(3, 7)
side.side(54)

# Problem 10
prob10 = Cosine(5,9)
angle_A = prob10.angle(7)
180 - angle_A

# Problem 11
prob11 = Cosine(12, 10)
d = prob11.side(90 + 50)
d

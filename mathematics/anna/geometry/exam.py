import numpy as np

class Circle():
    def __init__(self, r):
        self.radius = r
    def circumference(self):
        return 2*np.pi*self.radius
    def area(self):
        return np.pi * np.power(self.radius,2)

circ = Circle(r = 4)
circ.circumference()
circ.area()

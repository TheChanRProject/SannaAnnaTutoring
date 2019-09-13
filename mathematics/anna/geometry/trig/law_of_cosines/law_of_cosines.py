import numpy as np

class Cosine():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def side(self,angle):
        return np.sqrt(self.a**2 + self.b**2 - 2*self.a*self.b*np.cos(np.deg2rad(angle)))

    def side_squared(self,angle):
        return self.a**2 + self.b**2 - 2*self.a*self.b*np.cos(np.deg2rad(angle))

    def angle(self,c):
        argument = (c**2 - (self.a**2 + self.b**2)) / (2*self.a*self.b)
        return np.rad2deg(np.arccos(argument))

    def cos_angle(self, c):
        argument = (c**2 - (self.a**2 + self.b**2)) / (2*self.a*self.b)
        return argument

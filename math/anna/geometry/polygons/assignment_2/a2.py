import numpy

class Rectangle():
    def __init__(self, b, h):
        self.base_feet = b
        self.height_feet = h
        self.base_inches = b * 12
        self.height_inches = b * 12
    def feet_perimeter(self):
        return 2*self.base_feet + 2*self.height_feet
    def feet_area(self):
        return self.base_feet * self.height_feet
    def inches_area(self):
        return self.base_inches * self.height_inches
    def inches_perimeter(self):
        return 2*self.base_inches * self.height_inches


rec1 = Rectangle(18, 2)
rec1.feet_area()

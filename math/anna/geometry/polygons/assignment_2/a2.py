import numpy

class Rectangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def perimeter(self):
        return 2*self.base + 2*self.height
    def area(self):
        return self.base * self.height
        

import numpy as np

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
rec2 = Rectangle(6,24)
rec2.feet_area()
8.75 / 3.5

15 / 3
20 / 3
5 * 6.6666666667
rec3 = Rectangle(15,36)
rec3.feet_area()
540 / 100
5.4 * 70

rec4 = Rectangle(6, 300)
rec4.feet_area()
1800 / 400

18 * 4

rec5 = Rectangle(20, 30)

rec6 = Rectangle(26, 36).feet_area()
rec6

# Grass Problem
## Left Rectangle
g_rec1 = Rectangle(50,100)
g_rec1.feet_area()
a_rec1 = Rectangle(10,20)
a_rec1.feet_area()
a_rec2 = Rectangle(30,40)
a_rec2.feet_area()

left_rec_area = g_rec1.feet_area() - (a_rec1.feet_area() + a_rec2.feet_area())
print(left_rec_area)

g_rec2 = Rectangle(100, 100)
g_rec2.feet_area()
a_rec3 = Rectangle(20,15)
a_rec3.feet_area()
right_rec_area = g_rec2.feet_area() - a_rec3.feet_area()
print(right_rec_area)
print(left_rec_area + right_rec_area)

# Elephant Enclosure Problem

enclosure_1 = Rectangle(200, 500)
enclosure_1.feet_area()

enclosure_2 = Rectangle(1100, 180)
enclosure_2.feet_area()

enclosure_2.feet_area() > enclosure_1.feet_area()

class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return np.pi * np.power(self.radius, 2)

circ1 = Circle(2.5)
circ1.area()

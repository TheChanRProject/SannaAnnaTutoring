import math
import numpy as np

# def midpoint(x1,x2,y1,y2):
#     xC = (x1 + x2) / 2
#     yC = (y1 + y2) / 2
#     print(xC, yC)
#     return xC, yC
#
# midpoint(-1,4,5,-3)

def radius(x1,x2,y1,y2):
    pointSum = pow(x2-x1, 2) + pow(y2-y1, 2)
    distance = math.sqrt(pointSum)
    print(distance)
    return distance

radius(-1,1.5,5,1)

# def circum(r):
#     circumference = math.pi*2*r
#     print(circumference)
#     return circumference
#
# circum(4.7)
#
# def area(r):
#     areaC = math.pi*pow(r,2)
#     print(areaC)
#     return areaC
# area(4.7)
#

# print(rA / eL)

# rT = radius(-5, -10, -2, -2)
# aP = radius(-5, -8, 2, 2)
# hE = radius(-5, -2.5, 4, 4)
# pL = radius(-5, -3.5, 2, 2)
# hP = radius(-5, -5, 4, 2)
# pT = radius(-5, -5, 2, -2)
# rA = radius(-10, -8, -2, 2)
# eL = radius(-2.5,-3.5, 4, 2)
#
# help = [rT, pT, aP, rA]
# trap = [hP, hE, eL, pL]
#
# helpSum = sum(help)
# trapSum = sum(trap)

# height = (2*46)/23
# print(height)
#
# area = 2.5*3.5
# print(area/35)
#
# dif = math.sqrt(49 - 16)
# areaT = 0.5*dif*4
#
# newArea = 2*areaT + 99
# print(newArea)
#
# cirC = 14*math.pi
# print(cirC)

def ftToInch(x):
    return 12*x

def recPerimeter(l,w):
    return 2*l + 2*w


height = (2*13.16)/2.8
print(height)

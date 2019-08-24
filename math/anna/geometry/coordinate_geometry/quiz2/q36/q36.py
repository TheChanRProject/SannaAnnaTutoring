def q36_circle(x, y, r):
    circle = (x - 3)**2 + y**2
    if circle < r**2:
        print("Interior")
    elif circle == r**2:
        print("On the circle")
    elif circle > r**2:
        print("Exterior")
    return circle

A = (-1, 1)
B = (10, 0)
C = (4, -8)

q36_circle(A[0], A[1], 7)
q36_circle(B[0], B[1], 7)
q36_circle(C[0], C[1], 7)

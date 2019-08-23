import numpy as np

def distance(a: tuple,b: tuple):
    return np.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

np.sqrt(26) > 3*np.sqrt(2)

Q = (3,3)
R = (11 ,11)

QR = distance(Q, R)
print(QR)

WQ = (3*QR) / 4
print(WQ)

RW = QR / 4
print(RW)


128 / 16
72 - 18

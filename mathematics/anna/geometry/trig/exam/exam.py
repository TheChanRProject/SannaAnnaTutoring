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

# Problem 12
prob12 = Cosine(9, 13)
angle = prob12.angle(20)
180 - angle

# Problem 13
(20 * 7.5) / 1500
180 / 600
200 * 200

200000 / 280
240000 / 560
429 / 714

V_sheet_cake = 12 * 9 * 2
cal_V = V_sheet_cake / 3600
V_birthday_cake = np.pi * (4.5)**2 * 4

calories_birthday = cal_V * V_birthday_cake

calories_birthday
1.5 * 8
20 * 26
520 / 12

# Question 22
g_machine = (4/3)*np.pi * (9)**3
gumball = (4/3) * np.pi * (3/4)**3

g_machine / gumball

# Question 23

canister = np.pi * (1.5)**2 * 7
tennis_ball = (4/3)*np.pi * (2.25 / 2)**3

canister / tennis_ball
3 * tennis_ball
canister - (3 * tennis_ball)

def surface_area(l,w1, w2, lateral_h, base_h, base_shape: str):
    if base_shape == "triangle":
        lateral_area = (l+w1+w2)*lateral_h
        two_b = 2*(0.5)*l*base_h
    if base_shape == "rectangle":
        lateral_area = (2*l + w1 + w2)*lateral_h
        two_b = 2*l*base_h
    return lateral_area + two_b

print(surface_area(14, 13, 15, 20, 12, 'triangle'))

print(surface_area(5, 2, 2, 3, 2, "rectangle"))
96 * 96**0.5
96 /6
24 * 12
18 * *
18 * 8

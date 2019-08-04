def surface_area(l,w1, w2, lateral_h, base_h, base_shape: str):
    lateral_area = (l+w1+w2)*lateral_h
    if base_shape == "triangle":
        two_b = 2*(0.5)*l*base_h
    if base_shape == "rectangle":
        two_b = 2*l*base_h
    return lateral_area + two_b

print(surface_area(14, 13, 15, 20, 12, 'triangle'))

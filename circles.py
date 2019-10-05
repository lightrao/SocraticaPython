from math import pi


def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negtive number")
    if r < 0:
        raise ValueError("The radius can not be negative.")
    return pi * (r ** 2)


# Test function
radii = [2, 0, -3, 2 + 5j, True, "radius"]
massage = "Area of cicles with r={radius} is {area}"

for r in radii:
    A = circle_area(r)
    print(massage.format(radius=r, area=A))


print("aaa")

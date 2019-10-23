import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

# print(areas)

# Method 2: Use 'map' function
mp = map(area, radii)
print(mp)
areas = list(mp)
print(areas)
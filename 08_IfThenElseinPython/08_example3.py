# Isosceles triangle: Two sides have the same length.
# Equilateral triangle: All sids are equal.


a = int(input("The length of side a: "))
b = int(input("The length of side b: "))
c = int(input("The length of side c: "))


if a != b and b != c and c != a:
    print("This is a scalene triangle.")
elif a == b and b == c:
    print("This is an equilateral triangle.")
else:
    print("This is an isosceles triangle.")


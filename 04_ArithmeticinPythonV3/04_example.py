# Numbers: int, float, complex
# Operations: + - * /


x = 28  # int
print(type(x))
print(x)
y = 28.0  # float
print(type(y))
print(y)
z = float(28)  # float
print(type(z))
print(z)
a = 3.14  # float
print(type(a))
print(a)
b = int(3.14)  # int
print(type(int))
print(b)
# ints are narrower than floats
# floats are wider than ints


x = 1.732  # float
print(type(x))
print(x)
print(type(x + 0j))  # complex
print(x + 0j)
print(type(complex(x)))  # complex
print(complex(x))
# print(float(1.732 + 0j))
# floats are narrower than complex numbers
# complex numbers are wider than floats


a = 2 # int
b = 6.0 # float
c = 12 + 0j # complex
# Rule: Widen numbers so they are the same type
print(a + b)
print(b - a)
print(a * 7)
print(c / b)

# about division
print(16 / 5)
print(20 / 5)
print(16 % 5)
print(16 // 5)
# print(2/0)
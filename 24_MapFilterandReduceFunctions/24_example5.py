from functools import reduce

# Multiply all numbers in a list

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, z: x*z
z = reduce(multiplier, data)
print(z)

product = 1
for x in data:
    product = product * x

print(product)
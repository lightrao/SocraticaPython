squares = []
for i in range(1, 101):
    squares.append(i**2)
print(squares)

squares2 = [i**2 for i in range(1, 101)]
print(squares2)

remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)

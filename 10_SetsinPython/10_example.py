example = set()
# print(dir(example))
# print(help(example.add))


example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")
print(example)
example.add(42)
print(example)
print(len(example))
# print(help(example.remove))
example.remove(42)
print(len(example))
print(example)
# example.remove(50)
example.discard(50)
print(example)

example2 = set([28, True, 2.71828, "Helium"])
print(len(example2))
example2.clear()
print(len(example2))


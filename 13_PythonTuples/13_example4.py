# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
print(80*'-')

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
print(80*'-')

country = ("Australia")
print(country)
country = ("Australia",)
print(country)
print(80*'-')

a, b, c = (1, 2, 3, 4)
x, y, z = (1, 2)
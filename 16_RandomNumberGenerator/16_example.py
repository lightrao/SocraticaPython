import random

# Display 10 random numbers from interval [0, 1)
for i in range(10):
    print(random.random())
print(80*"-")

# Generate random numbers from interval [3, 7)
def my_random():
    # Random, scale, shift, return ...
    return 4*random.random() + 3

for i in range(10):
    print(my_random())    
print(80*"-")

for i in range(10):
    print(random.uniform(3, 7))
print(80*"-")

for i in range(20):
    print(random.normalvariate(0, 1))
print(80*"-")

for i in range(20):
    print(random.randint(1,6))
print(80*"-")

outcomes = ['rock', 'paper', 'scissors']
for i in range(20):
    print(random.choice(outcomes))
print(80*"-")
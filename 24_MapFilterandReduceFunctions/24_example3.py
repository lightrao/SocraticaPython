import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)
lu = list(filter(lambda x: x > avg, data))
print(lu)
ld = list(filter(lambda x: x < avg, data))
print(ld)

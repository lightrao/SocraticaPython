import timeit

list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print("List time: ", list_test)
print("Tuple time: ", tuple_test)
print(80*"-")

empty_tuple = ()
test1 = ("a",)
test2 = ("a", "b")
test3 = 'a', 'b', 'c'
print(empty_tuple)
print(test1)
print(test2)
print(test3)
print(80*"-")
test1 = 1, 
test2 = 1, 2
test3 = 1, 2, 3
print(test1)
print(test2)
print(test3)
print(type(test1))
print(type(test2))
print(type(test3))



# combine first name and last name into a single "Full Name"
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    leonhard", "EULER"))

l1 = lambda:"What is my purpose?"
print(l1())
l2 = lambda x:3*x + 1
print(l2(2))
l3 = lambda x, y:(x*y)**0.5 # Geometric Mean
print(l3(4,4))
l4 = lambda x, y, z: 3/(1/x + 1/y + 1/z) # Harmonic Mean
print(l4(1,2,3))
l5 = lambda x1,x2,x3,x4,x5: x1 + x2 + x3 + x4 + x5
print(l5(1, 2, 3, 4, 5))
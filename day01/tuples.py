# Intro to Tuples (tapl)
#   immutable
#   heterogeneous
#   name = ( e1, e2, ... )

t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

print(t1 + t2)
print(2 * t1)

# To get first element from tuple
print(t1[0])

# last element
print(t1[-1])

# ordered but not sorted
t3 = (2, 6, 1, 8, 30, 30, 100, 1)
print(t3)

# loop in tuple
for i in t1:
    print(i)

# loop in array
for i in [100, 200]:
    print(i)

# heterogeneous
my_tuple = (0, 1, "hi", (2, 3))

print(my_tuple[3][1])

# This just creates an integer...
# This creates a tuple
print(type((3)))
print(type((3,)))

t3 = t3.__add__((10000, 12))
print(t3)

# Your code here...
firstPart = my_tuple[:3]
lastPart = my_tuple[4:]

print(firstPart)
print(lastPart)
print(firstPart + (3,) + lastPart)


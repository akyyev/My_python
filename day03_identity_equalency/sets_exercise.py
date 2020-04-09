# Sets - Exercise

# 1. Check if ‘Eric’ and ‘John’ exist in friends
# 2. combine or add the two sets
# 3. Find names that are in both sets
# 4. find names that are only in friends
# 5. Show only the names who only appear in one of the lists
# 6. Create a new cars-list without duplicates

friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
cars = ['900', '420', 'V70', '911', '996', 'V90', '911', '911', 'S', '328', '900']

# 1. Check if ‘Eric’ and ‘John’ exist in friends
print("Eric", "John" in friends)

# 2. combine or add the two sets
print(friends.union(my_friends))

# 3. Find names that are in both sets
print(friends.intersection(my_friends))
print(friends & my_friends)

# 4. find names that are only in friends
print(friends.difference(my_friends))
print(friends - my_friends)
print(friends ^ my_friends)

# 5. Show only the names who only appear in one of the lists
print(friends.union(my_friends).difference(friends.intersection(my_friends)))

# 6. Create a new cars-list without duplicates
cars_set = set()
for car in cars:
    cars_set.add(car)

# ----or easier way-------
cars_set = set(cars)
print(cars_set)

# here is the set
list_of_cars = list(set(cars))

print(list_of_cars)

# -----------------------------------------
# sets are faster than both tuple and lists
# -----------------------------------------

# Question:
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to
# make a list whose elements are intersection of the above given lists.
#
# Hints:
# Use set() and "&=" to do set intersection operation.

set1 = set([1, 3, 6, 78, 35, 55])
set2 = set([12, 24, 35, 24, 55, 88, 120, 155])
set1 &= set2
li = list(set1)
print(li)
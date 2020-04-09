"""
This program shows how packing can use variables as elements in a list.
"""

x = 1
y = 2
z = 3
my_list = [x, y, z]

print(my_list)

# Assign multiple variables at a time, like this:
x, y, z = 1, 2, 3

# Assign multiple variables to a list (only if the number of variables
# is the SAME as the number of elements in the list.)
my_list = [10, 20, 30]
x, y, z = my_list

# A tuple can also be used
my_tuple = (1.0, 2.0, 3.0)
x, y, z = my_tuple



# Python program to demonstrate working
# of map.


# Return double of n
def double(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(double, numbers)
print(list(result))


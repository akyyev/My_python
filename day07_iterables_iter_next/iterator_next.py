# define a list
my_list = [4, 7, 0, -1]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

print(next(my_iter))  # 4
print(next(my_iter))  # 7
print(next(my_iter))  # 0
print(next(my_iter))  # -1


my_iter = iter(my_list)
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())


print("---------------")
# it's same as while loop underneath
for each in my_list:
    print(each)

print("---------------")
my_iter = iter(my_list)
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break


"""
-------------------What are generators in Python?----------------------------------
There is a lot of overhead in building an iterator in Python; we have to implement a class with __iter__() and
__next__() method, keep track of internal states, raise StopIteration when there was no values to be returned etc.

This is both lengthy and counter intuitive. Generator comes into rescue in such situations.

Python generators are a simple way of creating iterators.
All the overhead we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns an object (iterator)
which we can iterate over (one value at a time).


--------------------How to create a generator in Python?----------------------------
It is fairly simple to create a generator in Python.
It is as easy as defining a normal function with yield statement instead of a return statement.

If a function contains at least one yield statement (it may contain other yield or return statements),
it becomes a generator function. Both yield and return will return some value from a function.

The difference is that, while a return statement terminates a function entirely,
yield statement pauses the function saving all its states and later continues from there on successive calls
"""


def my_generator():
    n = 1
    print(f'This is printed first-{n}')
    yield n

    n += 1
    print(f'This is printed second-{n}')
    yield n

    n += 1
    print(f'This is printed last-{n}')
    yield n


a = my_generator()
# a1 = next(a)
# b1 = next(a)
# c1 = next(a)
# print(f"{a1}-{b1}-{c1}")
for each in my_generator():
    print(each)


def all_even():
    n = 0
    while True:
        yield n
        n += 2


ls = []
x = all_even()
for i in range(10):
    ls.append(next(x))

print(ls)

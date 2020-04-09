# Question:
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12

# Your program should accept a sequence of comma separated passwords
# and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
import re
import random


def validate_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    if not re.search('[$#@]', password):
        return False
    return True


def valid_passwords(passwords):
    ls = []
    for each in passwords.split(','):
        if validate_password(each):
            ls.append(each)
    print(ls)


# valid_passwords('ABd1234@1,a F1#,2w3E*,2We3345')


# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
# age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

def sort_tuples():
    tuples = []
    # to get records from user
    while True:
        inp = input('record: ')
        if not inp:
            break
        tuples.append(tuple(inp.split(',')))

    tuples.sort(key=lambda tup: (tup[0], tup[1], tup[2]))
    print(tuples)


# sort_tuples()

# Question:
# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

def getNumbers(num):
    i = 0
    for i in range(num):
        if i % 7 == 0:
            yield i


# first = getNumbers(100) # creates hundred record but we need to call for each one
# print(next(first))
# print(next(first))
def print_nums_div_by_7(how_many):
    for i in getNumbers(how_many):
        print(i)


# print_nums_div_by_7(100)


# Question£º
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

def frequency():
    # words = input('type a sentence: ').split()
    words = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'.split()
    dic = dict()
    for word in words:
        # we add word to the dictionary and assign the previous value plus 1.
        # if there is no such key we add new key with value of dic.get(word, 0) + 1 --> 0 +1 = 1
        # dic.get(word, 0) here 0 is default value if there is no such key
        dic[word] = dic.get(word, 0) + 1

    ls = sorted(dic.items(), key=lambda kv: (kv[0], kv[1]))
    for k, v in ls:
        print(k, v, sep=": ")


# frequency()

# Question:
# Define a function which can print a dictionary where the keys are
# numbers between 1 and 3 (both included) and the values are square of keys.

def dict_example(num):
    d = dict()
    for i in range(num + 1):
        d[str(i)] = i ** 2
    print(d.values())
    ls = list(d.values())
    print('Here are the first five numbers: ', ls[:5])
    print('Last five', ls[-5:])


# dict_example(20)

# Question:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
def square(num):
    return num * num


def m1():
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # map(func or lambda exp, iterable) returns map object then we can cast to list or tuple
    # squared_nums = map(square, ls)
    squared_nums = map(lambda x: x * x, ls)
    print(list(squared_nums))


# m1()


# Question:
# Write a program which can map() and filter() to make a list
# whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
def m2():
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = map(lambda x: x * x, filter(lambda x: x % 2 == 0, ls))
    print(list(even_numbers))


m2()


# Question:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
# even_nums = filter(lambda x: x % 2 == 0, range(1, 20))
# print(list(even_nums))


# Question:
# Define a class named American which has a static method called printNationality.

class American:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def printNationality():
        print('American')

    def greet(self):
        print('Hello', self.name)


class NewYorker(American):
    def __init__(self, name):
        super().__init__(name)


# anAmerican = American('John')
# anAmerican.printNationality()
# anAmerican.greet()
# American.printNationality()
# # American.greet()
# NewYorker.printNationality()
# p2 = NewYorker('Alex')
# p2.greet()


# Question:
# Please write a program using generator to print the numbers which can be divisible by 5 and 7
# between 0 and n in comma separated form while n is input by console.

def num_generate(num):
    for i in range(num):
        if i % 35 == 0:
            yield i


def m3(num):
    ls = []
    for i in num_generate(num):
        ls.append(i)
        assert i % 35 == 0  # to verify numbers are divisible by both 5 and 7
    print(ls)


# m3(100)


# Question: (Built in Evaluate function)
# Please write a program which accepts basic mathematic expression from console and print the evaluation result.
def m4(exp):
    print(eval(exp))


m4('5+10-5/2')

# Question: (random.random() module)
# Please generate a random float where the value is between 10 and 100 using Python math module.

num = random.random() * 100
print('Random number:', int(num))
print('Random choice from list:', random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(random.choice([i for i in range(11) if i % 2 == 0]))

# random list sample
ls = sorted(random.sample(range(100), 5))
print('Random sample list:', ls)
print('Random number in given range:', random.randrange(7, 16))
random.shuffle(ls)
print('Shuffled list:', ls)

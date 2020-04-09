# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
from pip._vendor.distlib.compat import raw_input


def print_tuple_list():
    numbers = input('Type numbers with comma: ').split(',')
    ls = list(int(e) for e in numbers)
    my_tuple = tuple(int(e) for e in numbers)
    print(ls, my_tuple, sep='\n')


# print_tuple_list()


# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class InputStringManipulate:
    def __init__(self):
        # __ makes str private
        self.__str = ""

    def get_string(self):
        self.__str = input('Enter some string: ')

    def print_str(self):
        print(self.__str.upper())


# my_str = InputStringManipulate()
# my_str.get_string()
# my_str.print_str()


# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

def create_2D_array(x, y):
    ls = []
    for i in range(x):
        temp = []
        for j in range(y):
            temp.append(i * j)
        ls.append(temp)
    return ls


def create_2D_array2(rows, columns):
    ls = [[row * col for col in range(columns)] for row in range(rows)]
    return ls


k = create_2D_array(3, 5)
s = create_2D_array2(3, 5)


# Question:
# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# words = input('Enter words with comma: ').split(',')
# words.sort()
# words = ','.join(word for word in words)
# # print(words)


# Question£º
# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
def some_method():
    ls = []
    while 1:
        r = raw_input()
        if r:
            ls.append(r)
        else:
            break
    for x in ls:
        print(x.upper())


# some_method()



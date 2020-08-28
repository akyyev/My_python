# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# from numpy import intp
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


# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words
# after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def remove_dup_words_and_sort():
    words = input('Type words with space: ').split()
    # sorted(ls-set-dict) returns sorted version, set() creates set with non-duplicates, list() converts to list
    res = ' '.join(sorted(list(set(words))))
    print(res)


# remove_dup_words_and_sort()


# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
def rem_non_divisible():
    items = input('numbers with comma: ').split(',')
    res = [int(e) for e in items if int(e, 2) % 5 == 0]
    print(res)


# rem_non_divisible()


# Question:
# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def some_nums_btn_1000_3000():
    ls = []
    for i in range(1000, 3000, 2):
        if int(i / 10) % 2 == 0 and int(i / 100) % 2 == 0 and int(i / 1000) % 2 == 0:
            ls.append(i)

    print(*[e for e in ls], sep=', ')


# some_nums_btn_1000_3000()


# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def calc_letter_digit():
    sentence = input('type some sentence: ')
    num_digit = 0
    num_letter = 0
    for i in sentence:
        if i.isdigit():
            num_digit += 1
        elif i.isalpha():  # isalpha check if character is letter or not
            num_letter += 1
    print('Letter:', num_letter)
    print('Numbers:', num_digit)


# calc_letter_digit()

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def special_calc(num):
    first = int('%s' % num)
    second = int('%s%s' % (num, num))
    third = int('%s%s%s' % (num, num, num))
    last = int('%s%s%s%s' % (num, num, num, num))
    print(first + second + third + last)


special_calc(9)




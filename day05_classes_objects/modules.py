# import platform, string, os, math
from math import pi
import string
from fractions import Fraction
# from os import mkdir as make_directory

print('Modules')
# https://docs.python.org/3/py-modindex.html
# Here are some most common modules
#                                   datetime random string os math browser


# print(dir(platform))
# print(platform.python_version())

# print(dir(os))
# print(os.mkdir("/Users/mac/PycharmProjects/My_python_project/some_file"))

print(dir(string))
print(string.ascii_letters)
print(string.capwords("python language", sep=" "))

# or we can import specific one to our project
# instead of this (import fractions) do this (from fractions import Fraction)
# print(fractions.Fraction(math.pi))
# print(884279719003555/281474976710656)

print(Fraction(pi))

# from os import mkdir as make_directory
# make_directory("SOME Path goes here")

import sys


# more ram efficient
def read(filename):
    f = open(filename, 'r')
    for line in f:
        print(line, end="")
    f.close()


# lesser efficient
def read2(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        print(line, end="")
    f.close()


# not efficient
def read3(filename):
    f = open(filename, 'r')
    text = f.read()
    print(text)
    f.close()


read3('/Users/mac/PycharmProjects/My_python_project/day10_classes/poem.txt')


def main():
    read(sys.argv[1])


if __name__ == '__main___':
    main()


def a():
    c()
    print("A")


def b():
    print("B")


def c():
    print("C")

c()


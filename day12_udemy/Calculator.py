# a = 10
#
# # Function will complain
# # def add():
# #     a += 10
# # add()
#
#
# print(a)


class Calculator:
    num = 100

    def __init__(self, a, b):
        self.f = a
        self.s = b
        print('Creation of object')

    def sum(self):
        res = self.f + self.s
        print("{} + {} = {}".format(self.f, self.s, res))

    def getData(self):
        print("({}, {})".format(self.f, self.s))


c1 = Calculator(3, 4)
c1.getData()
c1.sum()

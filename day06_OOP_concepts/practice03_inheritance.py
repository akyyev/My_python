'''
Encapsulation
Using OOP in Python, we can restrict access to methods and variables.
This prevent data from direct modification which is called encapsulation.
In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.
'''


class Computer:
    def __init__(self):
        self.__max_price = 900

    def sell(self):
        print(f"Selling Price: {self.__max_price}")

    def setMaxPrice(self, price):
        self.__max_price = price


c = Computer()
c.sell()
# print(c.__max_price)
c.setMaxPrice(1500)
c.sell()

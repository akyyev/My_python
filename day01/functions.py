# Nested functions
def printHello():
    name = input("Name: ")

    def m():
        t = 0
        for i in range(1, 11):
            t += i
        return t

    numberTotal = m()
    print(str(numberTotal) + " " + name)


printHello()

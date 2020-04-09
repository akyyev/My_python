# ZeroDivisionError
# print(5/0)


# TypeError
try:
    print(5 + "ab")
except TypeError:
    print("TypeError - You can't add directly like java")

# ValueError
try:
    num = int(input("Give me some number: "))
    print(num + 1)
except ValueError:
    print("Please type a number not a string")


# Exercise
def retrieve_positive_number():
    while True:
        res = -1
        try:
            res = int(input("Enter a positive number: "))
        except ValueError:
            print("Invalid number")
        if res > 0:
            break
    return res


print(retrieve_positive_number())

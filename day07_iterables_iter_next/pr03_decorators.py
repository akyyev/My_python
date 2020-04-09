def first(msg):
    print(msg)


# we can assign function name to a variable and use it later with passing values
second = first
second("Hello")


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    return func(x)


print(operate(inc, 5))
print(operate(dec, 4))


def smart_divide(func):
    def inner(a, b):
        print(f"I'm going to divide {a} with {b}!")
        if b == 0:
            print("Whoops! I cannot divide with zero")
            return
        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a / b


print(divide(3, 0))
print(divide(10, 2))



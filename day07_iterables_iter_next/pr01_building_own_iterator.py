"""Building an iterator from scratch is easy in Python. We just have to implement the methods __iter__() and
__next__(). """


class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    # Here, we show an example that will give us next power of 2 in each iteration.
    # Power exponent starts from zero up to a user set number.
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


for i in PowTwo(100):
    print(i)


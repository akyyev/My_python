def mystery(x):
    if type(x) is int:
        yield x
    else:
        for e in x:
            for y in mystery(e):
                yield y


ls = 1, [2, 3, 4, [5, 6, [], 7]]
output = [x for x in mystery(ls)]
print(output)


# a) (i) Mystery can accept integers and any list of lists with integers.
#    (ii) It flattens the list of lists and generates the list of integers by calling itself recursively.
# b) Higher order definition of mystery(x).


def mystery2(x, func):
    n = len(x)
    i = 0
    while i < n:
        func(x[i])
        i = i + 1


def thunk(x):
    if type(x) is int:
        ans.append(x)
    else:
        mystery2(x, thunk)


ls2 = [1], [2, [[3], 4], [5, [6, [], 7]]]
ans = []
mystery2(ls2, thunk)
print(ans)

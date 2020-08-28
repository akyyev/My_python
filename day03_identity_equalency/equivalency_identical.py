# Lists are equivalent but identical
ls = [1, 2, 3, 4]
ls2 = [1, 2, 3, 4]

# ls and ls3 are identical and equivalent --> True
ls3 = ls
print(ls is ls3)

print(ls is ls2)  # false
print(ls == ls2)  # true

# unpacking
coffee, tea, coke = ["dark blend", "herbal", "coca cola"]
print(coffee)  # dark blend


def pr(a, b, c):
    print(a + "-----" + b + "-----" + c)


pr(*["dark blend", "herbal", "coca cola"])

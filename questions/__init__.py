# gcd
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


print(gcd(15, 20))
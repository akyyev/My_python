# Normal list appending
ls = []

for i in range(1, 10):
    ls.append(i)

print(ls)

# This is better version
#     [(   ) (Now normal for loop)]
ls2 = [i * 2 for i in range(1, 10)]

print(ls2)

numbers = [pow(x, 3) for x in range(1, 10)]
print(numbers)

# Last names
names = [
    "Maya Angelou",
    "Chimamanda Ngozi Adichie",
    "Tobias Wolff",
    "Sherman Alexie",
    "Aziz Ansari"
]

# Your code here...
lastNames = [each.split()[-1] for each in names]
lastNames.sort()

print(lastNames)

#
list_of_strings = ["a", "2", "7", "zebra"]


def safe_int(ls1):
    res = [int(x) if x.isdigit() else 0 for x in ls1]
    print("If-else statement: ", res)

    newRes = [number for number in res if number > 0]
    print("List without zeros:", newRes)

    return res


print(safe_int(list_of_strings))

ls = [1, 2, 3, 4, 5, 6]
print([a for a in ls if a % 2 == 0])

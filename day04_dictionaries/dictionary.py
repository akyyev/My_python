# to create empty list
ls = []
ls1 = list()

# tuple
tp = ()
tp1 = tuple()

# set
# st = {} is wrong because {} will create dictionary
st = set()

# dictionary
dct = {}
dct1 = dict()

# get(key, optional output if not found) --> returns value
# pop(key) --> removes the key-value and returns value
# update()
# items() --> returns key,value tuples
# Example:
movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']
}
movie.update(
    {
        'title': 'The Holy Grail',
        'year': 1975,
        'cast': ['John', 'Terry', 'Michael']
    })

# since there is no budget key on dictionary it will add it to dictionary
movie['budget'] = 250000
movie["year"] = 2015
# to delete use del command
del movie["year"]
# movie.pop("title")

print(movie)
print("Printing first actor from cast: " + movie["cast"][0])

print(movie.keys())
print(movie.values())
print(movie.items())  # to print tuples

for key, value in movie.items():
    print(f"{key} -- {value}")


def week(i):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(i, "Invalid day of week")


print(week(5))
print(week(10))


def get_month(num):
    months = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }
    return months.get(num, 'illegal month input')


print(get_month(40))

months = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}

for key, value in months.items():
    print(key, value)


# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def create_dic():
    num = int(input('Size of dictionary: '))
    my_dict = {}
    for i in range(1, num + 1):
        my_dict[i] = i ** 2
    print(my_dict)


create_dic()

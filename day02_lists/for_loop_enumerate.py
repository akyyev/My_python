# enumerate is used to track the location of element
ls = "I like learning programming languages".split(" ")

for i, each in enumerate(ls):
    print(str(i + 1) + ": " + each)


# Example
def max_int_in_list(my_list):
    maxElement = my_list[0]
    ind = 0
    for i, element in enumerate(my_list):
        if element > maxElement:
            maxElement = element
            ind = i
    return my_list[ind]


list1 = [5, 2, -5, 10, 23, -21]
biggest_int = max_int_in_list(list1)
print(biggest_int)


#
def count_print(ls, target):
    count = 0
    for each in ls:
        if target in each.lower():
            count += 1
    print(f"There were {count} words that contained \"{target}\".")


ls = input("Enter some text: ").split()
count_print(ls, "owl")


my_list = [1, 5, 3, 7, 2]
my_dict = {'car': 4, 'dog': 2, 'add': 3, 'bee': 1}
my_tuple = ('d', 'c', 'e', 'a', 'b')
my_string = 'python'

print('original', my_dict)

my_list = [1, 5, -3, 7, -2]

print(sorted(my_list, key=abs))
print(my_list)  # my_list is still not sorted

my_list.sort()
my_list.reverse()
print('now it is sorted: ', my_list)

# to sort element based on index, we can use lambda functions
my_list2 = [['car', 4, 65], ['dog', 2, 30], ['add', 3, 10], ['bee', 1, 24]]
list2_sorted = sorted(my_list2, key=lambda item: item[1])
print(list2_sorted)
print('sorted based on last element', sorted(my_list2, key=lambda item: item[2]))




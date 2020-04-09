# append()
# extend()
# remove()

ls = []

ls.append(1)
ls.append(2)
ls.append((3, 4))  # adding tuple
ls.append([4])
ls.append("hi")
ls.append("hello")

print(ls)

# adding multiple elements -> extend()
ls.extend([5, 6, 7, 8, 9, 10])
ls.remove("hi")
print(ls)

# sort
# reverse
ls = ["10", "5", "20", "30", "hi", "hello"]
ls.sort()
ls.reverse()

print(ls)
# list = ([element])*number
#  ls1 = ([1]) * 3 --> [1, 1, 1]
ls = ([([0]) * 8]) * 8
print(ls)

# another example
ls = [([0]) * 8,
      ([0]) * 8,
      ([0]) * 8,
      ([0]) * 8,
      ([0]) * 8,
      ([0]) * 8,
      ([0]) * 8,
      ([0]) * 8]

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            ls[i][j] = 0
        else:
            ls[i][j] = 1

print(ls)

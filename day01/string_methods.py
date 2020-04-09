# upper()
# lower()
# len(str)
# isupper()
# islower()
# swapcase()
# strip() --> to remove whitespaces from starting and end
# find(st2) --> returns index if found
word = "Hello "
print(word.upper())
print(word.lower())
print(word.swapcase())
print(word.find("e"))
print(word.strip())
print(word.islower())
# index of o
print(word.find("o"))


def remove_all_from_string(st, st2):
    while st.find(st2) >= 0:
        num = st.find(st2)
        st = st[:num] + st[num + 1:]
    return st


print(remove_all_from_string("traditional", "a"))


def remove_all_from_string2(st, st2):
    while st.find(st2) >= 0:
        num = st.find(st2)
        st = st[:num] + st[num+len(st2):]
    return st


print(remove_all_from_string2("bananas", "na"))


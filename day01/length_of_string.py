st = "Me"

for i in range(len(st)):
    print(st[i])

my_string = "Mine"
for letter in my_string:
    print(letter)


# Contains vowel or not
def cont():
    word = input("Enter a string of lowercase letters: ")
    res = False
    for letter in word:
        res = res or letter in "aeiou"

    if res:
        print("Contains a lowercase vowel!")
    else:
        print("Doesn't contain a lowercase vowel.")


cont()

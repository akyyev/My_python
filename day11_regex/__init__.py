# search and replace
import re

st = 'My name is David, Hi David'
pattern = r'David'
new_st = re.sub(pattern, 'Amy', st)
print(new_st)

st2 = r'I am \r\a\w'  # r makes the string as raw string
print(st2)

# Metacharacters
# '.'   -- any character
# '^'   -- start
# '$'   -- end
# '[]'  -- any one match from specific char list


pattern = r'gr.y'
# re.match(pattern, 'matching_word)
print(re.match(pattern, 'grey'), re.match(pattern, 'gr-y'))
print(re.match(r'....K', 'any4K'))
print(re.match(r'^gr.y$', 'gray'))
print(re.match(r'..!', 'ca!'))  # 3 characters and last char is !
print(re.match('[loHeM]', 'Hello'))
print(re.match('[A-Za-z0-9]', 'Hello90'))
print(re.match('[A-Z][A-Z][0-9]', 'LS9'))

print(re.match('[1-5][0-9]', '59'))  # any number will match in range 10 to 59

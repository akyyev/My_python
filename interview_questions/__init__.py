def serialize(inp):
    def checkType(el):
        if type(el) == str:
            return "\"" + el + "\""
        elif type(el) == int:
            return el
        elif type(el) == list:
            ls = "["
            for m in el:
                ls += str(checkType(m)) + ", "
            ls = ls[:-2] + "]"
            return str(ls)

    with open('test2.json', 'w') as writer:

        if type(inp) == str:
            writer.write("\"" + inp + "\"")
        elif type(inp) == int:
            writer.write(str(inp))
        elif type(inp) == list:
            res = "["
            for e in inp:
                res += str(checkType(e)) + ", "
            res = res[:-2] + "]"
            writer.write(res)
        elif type(inp) == dict:
            res = "{"
            for key, value in inp.items():
                res += "\"" + str(key) + "\": "
                res += checkType(value) + ", "
            res = res[:-2] + "}"
            writer.write(res)


# serialize('this is a string') #-> "this is a string"
# serialize(5) -> 5
# serialize([1, 2, 3, 'four', [5, 6]]) -> [1, 2, 3, "four", [5, 6]]
# serialize({key1: 'value1', key2: [1, 2, 3, 'four', [5, 6]]})
#            -> {"key1": "value1", "key2": [1, 2, 3, "four", [5, 6]]}
# serialize([1, 2, 3, 'four', [5, 6]])
# print(type({'key1': 'value1', 'key2': [1, 2, 3, 'four', [5, 6]]}))
# print([value for key, value in {'key1': 'value1', 'key2': [1, 2, 3, 'four', [5, 6]]}.items()])

serialize('this is a string')
serialize({'key1': 'value1', 'key2': [1, 2, 3, 'four', [5, 6]], 5: 'five'})
# serialize(5)


def getFactorial(num):
    if num == 1:
        return 1
    else:
        return num * getFactorial(num - 1)


print(getFactorial(6))

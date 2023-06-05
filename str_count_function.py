def counter_un_letters(string):
    chars = {}
    res = 0
    temp = 0

    for i in string:
        if chars.get(i, 0):
            if temp > res:
                res = temp
            temp = 1
            chars = {}
        else:
            chars[i] = 1
            temp += 1

    return res


print(counter_un_letters('asdasdf'))

def rev_sen(string):
    res = string.split()
    for i in range(len(res)):
        res[i] = rev_word(res[i])

    rev_string = ''
    for i in range(len(res) - 1, -1, -1):
        rev_string += res[i] + ' '

    return rev_string


def rev_sen_2(string):
    res = string.split()
    res.reverse()

    for i in range(len(res)):
        res[i] = rev_word(res[i])

    return ' '.join(res)


def rev_word(word):
    res = ''

    for i in range(len(word) - 1, -1, -1):
        res += word[i]

    return res


print(rev_sen_2('?uoy era woh midaV olleH'))

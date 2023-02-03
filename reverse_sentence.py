def reverse_sentence(sen: str) -> str:
    rev_sen = ''
    for i in range(len(list(sen))):
        rev_sen += list(sen)[len(list(sen)) - 1 - i]
    return rev_sen


def reverse_words(sen: str) -> str:
    res = ''
    for i in range(len(sen.split()) - 1, -1, -1):
        res += sen.split()[i]
        res += ' '
    return res[:-1]


def reverse_words_2(sen: str) -> str:
    res = sen.split()
    res.reverse()
    return ' '.join(res)


print(reverse_words_2('snow dog sun'))

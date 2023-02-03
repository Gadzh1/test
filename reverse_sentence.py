def reverse_sentence(sen):
    rev_sen = ''
    for i in range(len(list(sen))):
        rev_sen += list(sen)[len(list(sen)) - 1 - i]
    return rev_sen


print(reverse_sentence('asd'))

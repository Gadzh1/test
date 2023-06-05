import random


def unique(listt):
    unique = []

    for i in listt:
        if not i in unique:
            unique.append(i)

    if len(unique) == len(listt):
        return True

    return False


def unique_dict(listt):
    unique = {}

    for i in listt:
        if i in unique:
            return False
        unique[i] = ''

    return True


numbers = []
for i in range(5):
    numbers.append(random.randrange(1, 10))

print(numbers)
print(unique_dict(numbers))

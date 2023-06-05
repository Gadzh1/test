import random


def count_it(sequence):
    num_inf = {}

    for i in sequence:
        if not int(i) in num_inf:
            num_inf[int(i)] = sequence.count(i)

    return num_inf


def count_it_2(sequence):
    num_inf = {}

    for i in sequence:
        if int(i) in num_inf:
            num_inf[int(i)] += 1
        else:
            num_inf[int(i)] = 1

    return num_inf


def count_it_3(sequence):
    num_inf = {}

    for i in sequence:
        num_inf[int(i)] = num_inf.get(int(i), 0) + 1

    return num_inf


numbers = ''

for i in range(5):
    numbers += str(random.randrange(0, 10))

print(numbers)
print(count_it(numbers))
print(count_it_2(numbers))
print(count_it_3(numbers))

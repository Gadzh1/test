def calc(num_1, num_2, action):
    if action == '+':
        return plus(num_1, num_2)

    if action == '-':
        return minus(num_1, num_2)

    if action == '*':
        return multiply(num_1, num_2)

    if action == '/':
        return divide(num_1, num_2)


def plus(num_1, num_2):
    return num_1 + num_2


def minus(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    return num_1 / num_2


print(calc(1, 1, '+'))

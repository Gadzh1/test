from math import gcd


class Fraction:
    def __init__(self, num, denom, integ=0):
        self.num = num + denom * integ
        self.denom = denom

    def __str__(self):
        integ = self.num // self.denom
        self.num %= self.denom
        nod = gcd(self.num, self.denom)

        if self.num == 0:
            return str(integ)

        if integ == 0:
            return f'{int(self.num / nod)}/{int(self.denom / nod)}'

        return f'{integ} {int(self.num / nod)}/{int(self.denom / nod)}'


def calc(num_1, num_2, action):
    if action == '+':
        return plus(num_1, num_2)

    if action == '-':
        return minus(num_1, num_2)

    if action == '*':
        return multiply(num_1, num_2)

    if action == '/':
        return divide(num_1, num_2)


def plus(fr_1, fr_2):
    if fr_1.denom == fr_2.denom:
        return Fraction(fr_1.num + fr_2.num, fr_1.denom)

    general_denom = fr_1.denom * fr_2.denom
    num_1 = fr_1.num * fr_2.denom
    num_2 = fr_2.num * fr_1.denom

    return Fraction(num_1 + num_2, general_denom)


def minus(fr_1, fr_2):
    if fr_1.denom == fr_2.denom:
        return Fraction(fr_1.num - fr_2.num, fr_1.denom)

    general_denom = fr_1.denom * fr_2.denom
    num_1 = fr_1.num * fr_2.denom
    num_2 = fr_2.num * fr_1.denom

    return Fraction(num_1 - num_2, general_denom)


def multiply(fr_1, fr_2):
    denom = fr_1.denom * fr_2.denom
    num = fr_1.num * fr_2.num

    return Fraction(num, denom)


def divide(fr_1, fr_2):
    denom = fr_1.denom * fr_2.num
    num = fr_1.num * fr_2.denom

    return Fraction(num, denom)


print(calc(Fraction(2, 3), Fraction(2, 5), '/'))

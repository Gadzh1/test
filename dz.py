def sum_func(n):
    n = str(n)
    return int(n) + int(n * 2) + int(n * 3)


def find_special_words(text):
    longest = ''
    most_frequent = ''
    amount = 1
    for i in text.split():
        if len(i) > len(longest):
            longest = i
        if amount < text.count(i):
            amount = text.count(i)
            most_frequent = i
    print(f'самое длинное слово {longest}\nсамое частое слово {most_frequent}, встречается {amount} разз')


listt = [15, 5, 30]

# print(list(filter(lambda n: n % 15 == 0, numbers)))
# print(sum_func(1))
find_special_words('lorem ipsum dolor sit amet amet amet sit sit')

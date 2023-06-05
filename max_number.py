def max_number(n1, n2):
    if n1 > n2:
        return n1
    return n2


amount = int(input()) - 1
biggest = int(input())
for i in range(amount):
    num = int(input())

    biggest = max_number(num, biggest)

print(biggest)

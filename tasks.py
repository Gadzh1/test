def binary_search(listt, num):
    left = 0
    right = len(listt) - 1
    middle = right // 2
    while True:
        if right - left == 1 or num < listt[0] or num > listt[right]:
            return -1
        if listt[middle] == num:
            return middle
        if listt[middle] > num:
            right = middle
        if listt[middle] < num:
            left = middle
        middle = (right + left) // 2


listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
print(binary_search(listt, 3))

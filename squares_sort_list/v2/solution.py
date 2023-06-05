def get_squares_sort_list(numbers):
    left = 0
    right = len(numbers) - 1

    res = [0] * len(numbers)
    index = right

    while left < right:
        l = numbers[left] * numbers[left]
        r = numbers[right] * numbers[right]

        if l < r:
            res[index] = r
            right -= 1
        else:
            res[index] = l
            left += 1

        index -= 1

    return res


print(get_squares_sort_list([-4, -1, 0, 3, 10]))

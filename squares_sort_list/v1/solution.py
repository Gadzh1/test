def get_squares_sort_list(listt):
    list_2 = []

    for i in listt:
        list_2.append(i * i)

    return sorted(list_2)


print(sort_nums([-4, -1, 0, 3, 10]))

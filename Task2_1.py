# Задание 2.1. В матрице найти номер строки, сумма чисел в которой максимальна

import sys

N = 5  # кол-во строк и столбцов

# функция для поиска строки с максимальной суммой


def col_max_sum(mat):
    idx = -1  # переменная для хранения индекса строки с максимумом
    max_sum = -sys.maxsize  # переменная для хранения максимальной суммы
    for i in range(0, N):
        sum_sum = 0
        for j in range(0, N):
            sum_sum += mat[i][j]
        if sum_sum > max_sum:
            max_sum = sum_sum
            idx = i
    res = [idx, max_sum]
    return res


mat = [[11, 21, 35, 40, 51], [15, 13, 10, 24, 52], [13, 16, 1, 8, 2], [0, 6, 3, 4, 12], [4, 7, 12, 4, 3]]
ans = col_max_sum(mat)

print("Row number ", ans[0]+1, "has max sumRow", ans[1])








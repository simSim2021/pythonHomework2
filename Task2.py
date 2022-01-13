# Задание 2.1. В матрице найти номер строки, сумма чисел в которой максимальна

import random
matrix = [[random.randint(-10, 10) for i in range(5)] for j in range(5)]
print("Исходная матрица: ", matrix)
s = []
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print("Строка с наибольшей суммой: ", matrix[s.index(max(s))], "Сумма элементов: ", max(s))

for index, value in enumerate(s):
    if value == max(s):
        print("Строка с наибольшей суммой: ", f'{index}: {value} ')


# print("Номер строки с наибольшей суммой: ", )
# import random
# a = []
# m = 0
# for i in range(5):
#    a.append([])
#    for j in range(5):
#        a[i].append(random.randint(1, 10))
#        print(a[i][j], end='')
#    print()
#    m = sum(a[i]) if sum(a[i]) > m else m
# print(m)



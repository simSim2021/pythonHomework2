# Задание 1.2
# Введите одномерный целочисленный список.
# Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.

import random

arr = []

for i in range(-30, -11):
    arr.append(i)
print(arr)

maxOdd = max((x for x in arr if x % 2 == 1), default=None)
if maxOdd is None:
    print("Такого числа нет")
else:
    print("Максимальное нечетное число ", maxOdd)

minMod = min(abs(i) for i in arr)

print("Минимальное по модулю число ", minMod)









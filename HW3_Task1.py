'''
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
'''

count= 0
i = 0
from random import randint
amountOfNumbers = int(input("Введите количество элементов в массиве: "))
numbers = [randint(0, 20) for num in range(amountOfNumbers)]
print("Полученный массив: ", numbers)
digit = int(input("Введите число, которое хотите найти в массиве: "))
for i in numbers:
    if i == digit:
        count += 1
print(count)



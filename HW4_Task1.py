'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
'''

value = [int(x) for x in input("Введите количество элементов n первого и m второго множества через пробел: ").split()]
n = value[0]
m = value[1]
set1 = set()
set2 = set()
list1 = list()
firstMn = [int(x) for x in input("Введите элементы первого множества через пробел: ").split()]
k1 = set(firstMn)
for i in k1:
    set1.add(i)
secondMn = [int(x) for x in input("Введите элементы второго множества через пробел: ").split()]
k2 = set(secondMn)
for i in k2:
    set2.add(i)
same = set1 & set2
same_ = list(same)
same_.sort()
for i in same_:
    print(i, end = ' ')
'''
 Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
'''

count= 0
i = 0
from random import randint
amountOfNumbers = int(input("Введите количество элементов в массиве: "))
numbers = [randint(0, 20) for num in range(amountOfNumbers)]
print("Полученный массив: ", numbers)
digit = int(input("Для какого числа будем искать ближайшее значение?: "))
numbers = set(numbers)
if digit in numbers:   
    numbers.remove(digit)
numbers = list(numbers)    
diff_numbers = []             
for i in numbers:
    num = abs(digit - i)    
    diff_numbers.append(num)        
minDifference = min(diff_numbers)                                              
ind = diff_numbers.index(minDifference)  
print(numbers[ind])                   
                                      

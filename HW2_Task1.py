'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''

quanityOfCoins = int(input("Введите количество монет: "))
countReshka = 0
countOrel = 0
for i in range(quanityOfCoins):
    coin = int(input("Как лежит монетка? Если решкой вверх, то 1, если орлом, то 0: "))
    if coin == 1:
        countReshka += 1
    if coin == 0:
        countOrel += 1
if countReshka < countOrel:
    print(countReshka)
else:
    print(countOrel)
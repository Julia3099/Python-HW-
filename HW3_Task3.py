'''
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12
'''

word = input("Введите слово: ")
word = list(word.upper())
result = 0
list1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']   # 1 очко
list2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']                                           # 2 очка
list3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']                                 # 3 очка
list4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']                            # 4 очка
list5 = ['K', 'Ж', 'З', 'Ц', 'Х', 'Ч']                                                # 5 очков
list6 = ['J', 'X', 'Ш', 'Э', 'Ю']                                           # 8 очков
list7 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']                                           # 10 очков                           # 5 очков

for i in word:
    if i in list1:
        result += 1
    elif i in list2:
        result += 2
    elif i in list3:
        result += 3
    elif i in list4:
        result += 4
    elif i in list5:
        result += 5
    elif i in list6:
        result += 8
    elif i in list7:
        result += 10
    else:
        print("Вводить можно только русские или английские буквы. Попробуйте ещё раз)")
print(result)




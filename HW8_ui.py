from logger import input_data, print_data, put_data, delete_data


def interface():
    command = -1
    while command != 5:
        print('Доброго времени суток! Что мы будем делать?\n'
              '1. Запишем данные(в 2-ух форматах)\n'
              '2. Удалим данные\n'
              '3. Изменим данные\n'
              '4. Выведем данные\n'
              '5. Выйдем из программы')
        command = int(input("Введите номер операции: "))

        while command < 1 or command > 5:
            print('Подумайте ещё раз) ')
            command = int(input("Введите номер операции: "))

        if command == 1:
            input_data()
        elif command == 2:
            delete_data()
        elif command == 3:
            put_data()
        elif command == 4:
            print_data()
        elif command == 5:
            print("Благодарим за уделённое время. Всего доброго!")
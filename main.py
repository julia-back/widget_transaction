import os


PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(os.path.dirname(__file__), "data")


def main():
    """Функция взаимодействия с пользователем и выстраивания основной логики проекта"""

    user_input = input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n""")
    if str(user_input) == "1":
        pass
        print("Для обработки выбран JSON-файл.")
    elif str(user_input) == "2":
        pass
        print("Для обработки выбран CSV-файл.")
    elif str(user_input) == "3":
        pass
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Некорректный ввод")

    while True:
        user_input = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""")
        if user_input.upper() == "EXECUTED":
            pass
            print("EXECUTED")
            break
        elif user_input.upper() == "CANCELED":
            pass
            print("CANCELED")
            break
        elif user_input.upper() == "PENDING":
            pass
            print("PENDING")
            break
        else:
            print(f"Статус операции \"{user_input}\" недоступен.")

    user_input = input("Отсортировать операции по дате? (Да/Нет)")
    pass
    user_input = input("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию)")
    pass
    user_input = input("Выводить только рублевые тразакции? Да/Нет")
    pass
    user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    pass

    print("Распечатываю итоговый список транзакций...")
    pass

    if есть транзакции:
        pass
        print(f"Всего банковских операций в выборке: {}")
        print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


main()

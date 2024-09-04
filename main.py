import os
from src import utils
from src import read_transactions
from config import DATA_PATH
from src import processing


file_json = os.path.join(DATA_PATH, "operations.json")
file_csv = os.path.join(DATA_PATH, "transactions.csv")
file_excel = os.path.join(DATA_PATH, "transactions_excel.xlsx")


def main():
    """Функция взаимодействия с пользователем и выстраивания основной логики проекта"""

    # Получаем от пользователя файл и выводим транзакции в виде списка словарей в переменной total_transactions
    total_transactions = []
    user_input = input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n""")
    if str(user_input) == "1":
        total_transactions = utils.get_read_json_file(file_json)
        print("Для обработки выбран JSON-файл.")
    elif str(user_input) == "2":
        total_transactions = read_transactions.reader_csv(file_csv)
        print("Для обработки выбран CSV-файл.")
    elif str(user_input) == "3":
        total_transactions = read_transactions.reader_excel(file_excel)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Некорректный ввод")

    # Получаем от пользователя статус и записываем отфильтрованный список словарей в переменную filtered_transactions
    while True:
        user_input = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""")
        if user_input.upper() == "EXECUTED":
            filtered_transactions = processing.filter_by_state(total_transactions)
            print("Операции отфильтрованы по статусу EXECUTED")
            break
        elif user_input.upper() == "CANCELED":
            filtered_transactions = processing.filter_by_state(total_transactions, state="CANCELED")
            print("Операции отфильтрованы по статусу CANCELED")
            break
        elif user_input.upper() == "PENDING":
            filtered_transactions = processing.filter_by_state(total_transactions, state="PENDING")
            print("Операции отфильтрованы по статусу PENDING")
            break
        else:
            print(f"Статус операции \"{user_input}\" недоступен.")

    # Уточняем у пользователя дополнительные параметры сортировки, записываем переменную sorted_transactions
    user_input = input("Отсортировать операции по дате? (Да/Нет)")
    if user_input.lower() == "да":
        user_input = input("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию)")
        if user_input.lower() == "по убыванию":
            sorted_transactions = processing.sort_by_date(filtered_transactions)
        elif user_input.lower() == "по возрастанию":
            sorted_transactions = processing.sort_by_date(filtered_transactions, reverse=False)
        else:
            print("Неверный ввод")
    elif user_input.lower() == "нет":
        sorted_transactions = filtered_transactions
    else:
        print("Неверный ввод")

    user_input = input("Выводить только рублевые тразакции? Да/Нет")
    if user_input.lower() == "да":
        pass
    elif user_input.lower() == "нет":
        pass
    else:
        print("Неверный ввод")
#     user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
#     pass
#
#     print("Распечатываю итоговый список транзакций...")
#     pass

    # if есть транзакции:
    #     pass
    #     print(f"Всего банковских операций в выборке: {}")
    #     print()
    # else:
    #     print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


main()

import os

from config import DATA_PATH
from src import generators, my_module, processing, read_transactions, utils, widget

file_json = os.path.join(DATA_PATH, "operations.json")
file_csv = os.path.join(DATA_PATH, "transactions.csv")
file_excel = os.path.join(DATA_PATH, "transactions_excel.xlsx")


def main():
    """Функция взаимодействия с пользователем и выстраивания основной логики проекта"""

    # Получаем от пользователя файл и выводим транзакции в виде списка словарей в переменной transactions
    transactions = []
    user_input = input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n""")
    if str(user_input) == "1":
        transactions = utils.get_read_json_file(file_json)
        print("Для обработки выбран JSON-файл.")
    elif str(user_input) == "2":
        transactions = read_transactions.reader_csv(file_csv)
        print("Для обработки выбран CSV-файл.")
    elif str(user_input) == "3":
        transactions = read_transactions.reader_excel(file_excel)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Некорректный ввод")

    clear_transactions = []
    for transaction in transactions:
        if type(transaction) is not None:
            clear_transactions.append(transaction)
    transactions = clear_transactions

    # Получаем от пользователя статус и перезаписываем отфильтрованный список словарей в переменную transactions
    while True:
        user_input = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""")
        if user_input.upper() == "EXECUTED":
            transactions = processing.filter_by_state(transactions)
            print("Операции отфильтрованы по статусу EXECUTED")
            break
        elif user_input.upper() == "CANCELED":
            transactions = processing.filter_by_state(transactions, state="CANCELED")
            print("Операции отфильтрованы по статусу CANCELED")
            break
        elif user_input.upper() == "PENDING":
            transactions = processing.filter_by_state(transactions, state="PENDING")
            print("Операции отфильтрованы по статусу PENDING")
            break
        else:
            print(f"Статус операции \"{user_input}\" недоступен.")

    # Уточняем у пользователя дополнительные параметры сортировки
    user_input = ""
    while user_input.lower() != "нет":
        user_input = input("Отсортировать операции по дате? (Да/Нет)\n")
        if user_input.lower() == "да":
            user_input = input("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию)\n")
            if user_input.lower() == "по убыванию":
                transactions = processing.sort_by_date(transactions)
                break
            elif user_input.lower() == "по возрастанию":
                transactions = processing.sort_by_date(transactions, reverse=False)
                break

    while True:
        user_input = input("Выводить только рублевые тразакции? Да/Нет\n")
        if user_input.lower() == "да":
            transactions_generator = generators.filter_by_currency(transactions, "RUB")
            break
        elif user_input.lower() == "нет":
            transactions_generator = transactions
            break
#
    print(transactions_generator)

    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        if user_input.lower() == "да":
            user_input = input("Введите слово для фильтрации\n")
            transactions = my_module.get_search(transactions_generator, user_input)
            break
        elif user_input.lower() == "нет":
            transactions = []
            for transaction in transactions_generator:
                transactions.append(transaction)
            break

    print(transactions)

    # Вывод списка транзакций
    print("Распечатываю итоговый список транзакций...")
    if len(transactions) != 0:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            date = widget.get_date(transaction.get("date"))
            description = transaction.get("description")
            card_to = widget.mask_account_card(transaction.get("to"))
            amount = round(float(transaction.get("operationAmount").get("amount")))
            name = transaction.get("operationAmount").get("currency").get("name")
            if transaction.get("from") is not None:
                card_from = widget.mask_account_card(transaction.get("from"))
                print(f"{date} {description}\n{card_from} -> {card_to}\nСумма: {amount} {name}\n\n")
            else:
                print(f"{date} {description}\n{card_to}\nСумма: {amount} {name}\n\n")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


main()

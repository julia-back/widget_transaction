import collections
import re


def get_search(transactions, search_str: str) -> list[dict]:
    """
    Функция для поиска по транзакциям. Принимает список словарей с транзакциями и строку для поиска.
    Возвращает список словарей, в которых есть данная строка
    """
    transactions_by_search = []

    for transaction in transactions:
        if type(transaction) is not None:
            if re.search(search_str, str(transaction), flags=re.IGNORECASE):
                transactions_by_search.append(transaction)
    return transactions_by_search


def get_count_transactions(transactions: list[dict], user_categories: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    descriptions = []
    for transaction in transactions:
        descriptions.append(transaction.get("description"))
    count_user_category = []
    for category in user_categories:
        for description in descriptions:
            if category.lower() == description.lower():
                count_user_category.append(description)
    return collections.Counter(count_user_category)

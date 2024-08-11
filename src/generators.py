def filter_by_currency(transactions, code):
    """
    Принимает на вход список словарей, представляющих транзакции, и код валюты для фильтрации, возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    filter_transactions = (t for t in transactions if t["operationAmount"]["currency"]["code"] == code)
    return filter_transactions


def transaction_descriptions(transactions):
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]



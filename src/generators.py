def filter_by_currency(transactions, code: str):
    """
    Принимает на вход список словарей, представляющих транзакции, и код валюты для фильтрации, возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    if len(transactions[0]) > 7:
        filter_transactions = (t for t in transactions if t.get("currency_code") == code)
    else:
        filter_transactions = (t for t in transactions if t.get("operationAmount").get("currency").get("code") == code)
    return filter_transactions


def transaction_descriptions(transactions) -> dict:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int | str, stop) -> str:
    """
    Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Принимает начальное и конечное значения для генерации диапазона номеров.
    """
    for num in range(int(start), int(stop) + 1):
        nums = "0000000000000000" + str(num)
        yield nums[-16:-12] + " " + nums[-12:-8] + " " + nums[-8:-4] + " " + nums[-4:]

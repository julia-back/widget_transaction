import os

import dotenv
import requests


def get_conversion_to_rubles(transaction: dict[str, str | int | dict[str, str | int | dict[str | int]]]) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    """
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?amount={amount}&from={currency}&to=RUB"
        dotenv.load_dotenv()
        api_key = os.getenv("API_KEY")
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers).json()
        amount = response["result"]
        return round(amount, 2)

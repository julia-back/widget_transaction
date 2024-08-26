import json
import os

import dotenv
import requests


def get_conversion_to_rubles(transaction: dict[str]) -> float:
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
        responce = requests.get(url, headers=headers)
        with open("convert.json", "w", encoding="utf-8") as convert_file:
            convert_file.write(responce.text)
        with open("convert.json", "r", encoding="utf-8") as convert_file:
            convert_dict = json.load(convert_file)
            amount = convert_dict["result"]
            return round(amount, 2)




print(get_conversion_to_rubles({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }))

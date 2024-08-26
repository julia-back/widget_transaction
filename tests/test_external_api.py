from src.external_api import get_conversion_to_rubles
from unittest.mock import patch


def test_conversion_to_rubles_rub():
    assert get_conversion_to_rubles({"id": 441945886,
                                     "state": "EXECUTED",
                                     "date": "2019-08-26T10:50:58.294041",
                                     "operationAmount": {"amount": "31957.58",
                                                         "currency": {"name": "руб.",
                                                                      "code": "RUB"}},
                                     "description": "Перевод организации",
                                     "from": "Maestro 1596837868705199",
                                     "to": "Счет 64686473678894779589"}) == "31957.58"


@patch("requests.get")
def test_conversion_to_rubles_usd(mock_get):
    mock_get.return_value.json.return_value = {"success": True,
                                               "query": {
                                                   "from": "USD",
                                                   "to": "RUB",
                                                   "amount": 8221.37},
                                               "info": {
                                                   "timestamp": 1724711523,
                                                   "rate": 92.000502},
                                               "date": "2024-08-26",
                                               "result": 756370.167128}
    assert get_conversion_to_rubles({"id": 41428829,
                                     "state": "EXECUTED",
                                     "date": "2019-07-03T18:35:29.512364",
                                     "operationAmount": {
                                         "amount": "8221.37",
                                         "currency": {
                                             "name": "USD",
                                             "code": "USD"}},
                                     "description": "Перевод организации",
                                     "from": "MasterCard 7158300734726758",
                                     "to": "Счет 35383033474447895560"}) == 756370.17


@patch("requests.get")
def test_conversion_to_rubles_eur(mock_get):
    mock_get.return_value.json.return_value = {"success": True,
                                               "query": {
                                                   "from": "EUR",
                                                   "to": "RUB",
                                                   "amount": 8221.37},
                                               "info": {
                                                   "timestamp": 1724711523,
                                                   "rate": 92.000502},
                                               "date": "2024-08-26",
                                               "result": 756370.167128}
    assert get_conversion_to_rubles({"id": 41428829,
                                     "state": "EXECUTED",
                                     "date": "2019-07-03T18:35:29.512364",
                                     "operationAmount": {
                                         "amount": "8221.37",
                                         "currency": {
                                             "name": "EUR",
                                             "code": "EUR"}},
                                     "description": "Перевод организации",
                                     "from": "MasterCard 7158300734726758",
                                     "to": "Счет 35383033474447895560"}) == 756370.17

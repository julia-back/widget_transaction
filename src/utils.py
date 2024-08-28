import json
import logging


def get_read_json_file(json_file: str) -> list[dict[str, str]]:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            file_data = json.load(file)
    except FileNotFoundError:
        print("Файл не найден или указан некорректный путь")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []
    else:
        if type(file_data) is list:
            return file_data
        else:
            return []

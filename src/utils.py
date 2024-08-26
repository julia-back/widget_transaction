import json
import os

from main import PATH


def get_read_json_file(json_file: str) -> list[dict[str, str]]:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    file_data = []
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            file_data = json.load(file)
    except FileNotFoundError:
        print("Файл не найден или указан некорректный путь")
        return file_data
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return file_data
    else:
        if type(file_data) is list:
            return file_data
        else:
            return file_data


print(get_read_json_file(os.path.join(PATH, "data", "operations.json")))

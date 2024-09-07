import json
import logging
import os

from config import PATH

logging.basicConfig(filemode="w")
logger = logging.getLogger("utils.py")
handler = logging.FileHandler(os.path.join(PATH, "logs", "logs_utils.log"))
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def get_read_json_file(json_file: str) -> list[dict[str, str]]:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    logging.info(f"Start read file {json_file}")
    try:
        logging.info(f"Opening file {json_file}")
        with open(json_file, "r", encoding="utf-8") as file:
            file_data = json.load(file)
    except FileNotFoundError as ex:
        logging.error(f"{ex}: file not found at this path")
        return []
    except json.JSONDecodeError as ex:
        logging.error(f"{ex}: error decoding file")
        return []
    else:
        logging.info(f"Open file {json_file}")
        if type(file_data) is list:
            return file_data
        else:
            return []

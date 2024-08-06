from typing import Any, Iterable, Optional


def filter_by_state(list_of_dictionary: Iterable[Any], state: Optional[str] = "EXECUTED") -> Iterable[Any]:
    """Принимает список словарей  и опционально параметр, возвращает новый список словарей"""
    list_by_state = []
    for dictionary in list_of_dictionary:
        if dictionary["state"] == state:
            list_by_state.append(dictionary)
    return list_by_state


def sort_by_date(list_of_dictionary: Iterable[Any], reverse: bool = True) -> Iterable[Any]:
    """
    Принимает список словарей и опционально порядок сортировки (по умолчанию - по убыванию),
    возвращает новый отсортированный по дате список словарей
    """
    list_by_date = sorted(list_of_dictionary, reverse=reverse, key=lambda x: x["date"])
    return list_by_date

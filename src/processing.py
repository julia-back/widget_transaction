def filter_by_state(list_of_dictionary: list, state="EXECUTED") -> list:
    """Принимает список словарей  и опционально параметр, возвращает новый список словарей"""
    list_by_state = []
    for dictionary in list_of_dictionary:
        if dictionary["state"] == state:
            list_by_state.append(dictionary)
    return list_by_state

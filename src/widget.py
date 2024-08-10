def mask_account_card(kind_and_numbers: str) -> str:
    """Принимает строку с типом и номером карты или счета,возвращает её с замаскированным номером"""
    from src import masks
    kind = ""
    numbers = ""
    for symbol in kind_and_numbers:
        if symbol.isalpha() or symbol.isspace():
            kind += symbol
        elif symbol.isdigit():
            numbers += symbol
    # Очистим строку типа карты или счета от пробелов
    kind_clean = ""
    for letter in kind:
        if letter.isalpha():
            kind_clean += letter
    # Добавим пробел перед большой, если тип карты или счета состоит из двух или более слов
    kind_list = list(kind_clean)
    i = 1
    while i < len(kind_list):
        if kind_list[i].isupper():
            kind_list.insert(i, " ")
            i += 1
        i += 1
        kind_clean = "".join(kind_list)
    # Выведем результат в зависимости от типа карты или счета
    if kind_clean.lower() == "счет":
        mask_account = masks.get_mask_account(int(numbers))
        return kind_clean + " " + mask_account
    else:
        mask_card = masks.get_mask_card_number(int(numbers))
        return kind_clean + " " + mask_card


def get_date(complication_data: str) -> str:
    """Функция преобразует кашу из символов в нормальную дату 'дд.мм.гггг'"""
    if len(complication_data) > 0:
        date = f"{complication_data[8:10]}.{complication_data[5:7]}.{complication_data[:4]}"
        return date
    else:
        raise ValueError

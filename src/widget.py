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
    if kind.lower() == "счет ":
        mask_account = masks.get_mask_account(int(numbers))
        return kind + mask_account
    else:
        mask_card = masks.get_mask_card_number(int(numbers))
        return kind + mask_card


print(mask_account_card("Visa Platinum 8990922113665229"))


def get_date(complication_data: str) -> str:
    """Функция преобразует кашу из символов в нормальную дату 'дд.мм.гггг'"""
    return f"{complication_data[8:10]}.{complication_data[5:7]}.{complication_data[:4]}"


print(get_date("2024-03-11T02:26:18.671407"))

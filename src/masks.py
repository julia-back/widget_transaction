def get_mask_card_number(card_num: str | int) -> str:
    """Принимает номер карты и маскирует цифры, кроме первых шести и последних четырех цифр"""
    if str(card_num).isdigit():
        if len(str(card_num)) >= 10:
            mask_num = str(card_num)[:4] + " " + str(card_num)[4:6] + "** **** " + str(card_num)[-4:]
            return mask_num
        else:
            raise ValueError
    else:
        raise TypeError


def get_mask_account(account_num: str | int) -> str:
    """Принимает номер счета и возвращает две звездочки и последние четыре цифры"""
    if len(str(account_num)) >= 4:
        return "**" + str(account_num)[-4:]
    else:
        raise ValueError

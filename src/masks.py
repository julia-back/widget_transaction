def get_mask_card_number(card_num: int) -> str:
    """Принимает номер карты и маскирует цифры, кроме первых шести и последних четырех цифр"""
    mask_num = str(card_num)[:4] + " " + str(card_num)[4:6] + "** **** " + str(card_num)[-4:]
    return mask_num


def get_mask_account(account_num: int) -> str:
    """Принимает номер счета и возвращает две звездочки и последние четыре цифры"""
    return "**" + str(account_num)[-4:]

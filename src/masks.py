import logging
import os

from main import PATH

logging.basicConfig(filemode="w")
logger = logging.getLogger("masks.py")
handler = logging.FileHandler(os.path.join(PATH, "logs", "logs_masks.log"))
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_num: str | int) -> str:
    """Принимает номер карты и маскирует цифры, кроме первых шести и последних четырех цифр"""
    logger.info(f"Start mask card numbers: {card_num}")
    if str(card_num).isdigit():
        if len(str(card_num)) >= 10:
            mask_num = str(card_num)[:4] + " " + str(card_num)[4:6] + "** **** " + str(card_num)[-4:]
            logging.info(f"Mask numbers from {card_num} to {mask_num}")
            return mask_num
        else:
            logging.error(f"Error. Too short argument {card_num}")
            raise ValueError
    else:
        logging.error(f"Error. Argument {card_num} is not digit")
        raise TypeError


def get_mask_account(account_num: str | int) -> str:
    """Принимает номер счета и возвращает две звездочки и последние четыре цифры"""
    logger.info(f"Start mask account numbers: {account_num}")
    if len(str(account_num)) >= 4:
        mask_account = "**" + str(account_num)[-4:]
        logging.info(f"Mask account numbers from {account_num} to {mask_account}")
        return mask_account
    else:
        logging.error(f"Too short argument {account_num}")
        raise ValueError

import pytest
from src import masks


@pytest.fixture
def numbers_card():
    return 7000792289606361


def test_get_mask_card_number(numbers_card):
    assert masks.get_mask_card_number(numbers_card) == "7000 79** **** 6361"


def test_get_mask_card_number_is_no_digit():
    with pytest.raises(TypeError):
        assert masks.get_mask_card_number("ogiuog")


def test_get_mask_card_small():
    with pytest.raises(ValueError):
        assert masks.get_mask_card_number(76)


@pytest.mark.parametrize("card_num, expected", [(7964974869760787970979808758465495786979, "7964 97** **** 6979"),
                                                ("7964974869760787970979808758465495786979", "7964 97** **** 6979")])
def test_get_mask_card_number_by_parametrize(card_num, expected):
    assert masks.get_mask_card_number(card_num) == expected


@pytest.mark.parametrize("account_num, expected", [(73654108430135874305, "**4305"),
                                                   (786869876987687687687687689769876876879876987698, "**7698"),
                                                   ("769874568765", "**8765")])
def test_get_mask_account(account_num, expected):
    assert masks.get_mask_account(account_num) == expected


def test_get_mask_account_error():
    with pytest.raises(ValueError):
        assert masks.get_mask_account(76)

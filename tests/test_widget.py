import pytest
from src import widget


@pytest.mark.parametrize("kind_and_numbers, expected",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                          ("Счет 73654108430135874305", "Счет **4305"),
                          ("Very BadCard      87608968658764685 65086986086087", "Very Bad Card 8760 89** **** 6087")])
def test_mask_account_card(kind_and_numbers, expected):
    assert widget.mask_account_card(kind_and_numbers) == expected


def test_get_date():
    assert widget.get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_none():
    with pytest.raises(ValueError):
        widget.get_date("")

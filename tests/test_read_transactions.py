import os.path
from unittest.mock import Mock

import pandas as pd

from main import DATA_PATH
from src import read_transactions


def test_reader_csv():
    pd.read_csv = Mock(return_value=pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))
    assert read_transactions.reader_csv(os.path.join(DATA_PATH, "operations.json")) == [{'No': 131, 'Yes': 50},
                                                                                        {'No': 2, 'Yes': 21}]


def test_reader_excel():
    pd.read_excel = Mock(return_value=pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))
    assert read_transactions.reader_excel(os.path.join(DATA_PATH, "operations.json")) == [{'No': 131, 'Yes': 50},
                                                                                          {'No': 2, 'Yes': 21}]

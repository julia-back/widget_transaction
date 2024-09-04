import json
import os
from unittest.mock import Mock

from config import PATH
from src.utils import get_read_json_file


def test_get_read_json_file_ok():
    json.load = Mock(return_value=[{"1": "1"}, {"2": "2"}])
    assert get_read_json_file(os.path.join(PATH, "data", "operations.json")) == [{"1": "1"}, {"2": "2"}]


def test_get_read_json_file_not_found_file():
    assert get_read_json_file("") == []


def test_get_read_json_file_is_not_list():
    json.load = Mock(return_value={})
    assert get_read_json_file(os.path.join(PATH, "data", "operations.json")) == []

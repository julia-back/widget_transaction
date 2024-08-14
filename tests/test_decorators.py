from src.decorators import log


# Testing functions for test log
@log(filename="logs.txt")
def func_and_file(x, y):
    return x / y


@log()
def func_no_file(x, y):
    return x / y


# Tests for log
def test_log_file(filename="logs.txt"):
    func_and_file(2, 2)
    with open(filename, "r", encoding="utf-8") as file:
        last_lines = file.readlines()[-4:]
        assert last_lines == ["Function func_and_file started\n", "Function func_and_file finished\n",
                              "Result: 1.0\n", "\n"]


# def test_log_print():
#     result = func_no_file(2, 2)
#     assert result == 1


def test_log_file_error(filename="logs.txt"):
    func_and_file(2, 0)
    with open(filename, "r", encoding="utf-8") as file:
        last_lines = file.readlines()[-5:]
        assert last_lines == ["Function func_and_file started\n", "Function func_and_file finished by error:\n",
                              "<class 'Exception'>:division by zero\n", "Parameters - args: (2, 0), kwargs: {}\n", "\n"]


# def test_log_error_2():
#     func_no_file(2, 0)

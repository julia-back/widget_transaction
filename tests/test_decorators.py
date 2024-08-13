from src.decorators import log


# Testing functions for test log
@log(filename="logs.txt")
def func_and_file(x, y):
    return x / y


@log()
def func_no_file(x, y):
    return x / y

#
def test_log_1():
    result = func_and_file(2, 2)
    assert result == 1


def test_log_2():
    result = func_no_file(2, 2)
    assert result == 1


def test_log_error():
    func_and_file(2, 0)



def test_log_error_2():
    func_no_file(2, 0)

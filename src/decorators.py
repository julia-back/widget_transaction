from functools import wraps
from time import time


def log(filename=None):
    """
    Декоратор для логирования вызова функции.
    Принимает опциональный аргумент - файл для записи логов. По умолчанию выводит логи в консоль.
    Выводит время начала работы функции, время ококнчания работы функции,
    в случае успеха выводит результат выполнения функции,
    в случае ошибки выводит тип и описание ошибки, а также входные данные функции.
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            time_start = time()
            try:
                result = func(*args, **kwargs)
            except Exception as error_info:
                time_stop = time()
                if filename is None:
                    print(f"Function {func.__name__} started in {time_start}\n"
                          f"Function {func.__name__} finished in {time_stop} by error:\n{Exception}: {error_info}\n"
                          f"Parameters - args: {args}, kwargs: {kwargs}\n")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Function {func.__name__} started in {time_start}\n"
                                   f"Function {func.__name__} finished in {time_stop} by error:\n{Exception}:{error_info}\n"
                                   f"Parameters - args: {args}, kwargs: {kwargs}\n\n")
            else:
                time_stop = time()
                if filename is None:
                    print(f"Function {func.__name__} started in {time_start}\n"
                          f"Function {func.__name__} finished in {time_stop}\n"
                          f"Result: {result}\n")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Function {func.__name__} started in {time_start}\n"
                                   f"Function {func.__name__} finished in {time_stop}\n"
                                   f"Result: {result}\n\n")
                return result
        return inner
    return wrapper

from typing import Callable


def deanon(func: Callable) -> Callable:

    def inner(*args, **kwargs) -> tuple:
        return func.__name__, func(*args, **kwargs)
    return inner

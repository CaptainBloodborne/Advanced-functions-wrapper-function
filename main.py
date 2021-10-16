from typing import Callable


def deanon(func: Callable) -> Callable:

    def inner(*args, **kwargs) -> tuple:
        return (func.__name__, func(*args, **kwargs))

    if not isinstance(func, callable):
        raise NotImplementedError('Implement me!')
    return inner

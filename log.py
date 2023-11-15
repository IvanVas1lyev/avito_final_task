from typing import Callable
from random import randint


def log(text: str) -> Callable:
    """
    Decorates function
    
    Parameters
    ----------
    text : str
        Text for decorator
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            print(text.format(randint(15, 50)))

            return ret

        return wrapper

    return decorator

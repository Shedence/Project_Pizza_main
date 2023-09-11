from functools import wraps
from random import randint


def log(text=str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            p = randint(10, 30)
            print(f" {text} {p} минут.")
        return wrapper
    return decorator

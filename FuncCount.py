from functools import wraps


def counter(func):
    count = 0

    @wraps(func)
    def wrap(*args, **kwargs):
        nonlocal count
        count += 1
        return func(*args, **kwargs)

    def counter():
        return count

    setattr(wrap, "counter", counter)
    return wrap


import sys

exec(sys.stdin.read())

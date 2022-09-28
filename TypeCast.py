from functools import wraps


def cast(typ):
    def inner_cast(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            return typ(func(*args, **kwargs))
        return wrap
    return inner_cast

import sys

exec(sys.stdin.read())

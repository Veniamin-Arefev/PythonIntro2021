from functools import wraps
import inspect


def dec(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        args_names, star_args_name, star_kwargs_name, defaults, \
        kwonlyargs, kwonlydefaults, annotations = inspect.getfullargspec(fun)

        # print("     ", args_names, star_args_name, star_kwargs_name, defaults, kwonlyargs, kwonlydefaults, annotations)
        # print("     ", "TAKI CALL", args, kwargs)

        for argument_index, argument in enumerate(args):
            if argument_index >= len(args_names):  # should check star_args_name type only
                if star_args_name in annotations:
                    if not isinstance(argument, annotations[star_args_name]):
                        raise TypeError(f"Type mismatch: {star_args_name}")
            else:
                if args_names[argument_index] in annotations:
                    if not isinstance(argument, annotations[args_names[argument_index]]):
                        raise TypeError(f"Type mismatch: {args_names[argument_index]}")

        for argument_name, argument in kwargs.items():
            if argument_name in annotations:
                if not isinstance(argument, annotations[argument_name]):
                    raise TypeError(f"Type mismatch: {argument_name}")
            else:
                if star_kwargs_name in annotations:
                    if not isinstance(argument, annotations[star_kwargs_name]):
                        raise TypeError(f"Type mismatch: {star_kwargs_name}")

        ret_val = fun(*args, **kwargs)
        argument_name = "return"
        if argument_name in annotations:
            if not isinstance(ret_val, annotations[argument_name]):
                raise TypeError(f"Type mismatch: {argument_name}")
        return ret_val

    return wrapper


class checked(type):

    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)

    def __new__(cls, name, parents, ns):
        # print("new", cls, name, parents, ns)
        for field in ns:
            if hasattr(ns[field], "__annotations__"):
                ns[field] = dec(ns[field])
        return super().__new__(cls, name, parents, ns)

    def __init__(self, name, parents, ns):
        super().__init__(name, parents, ns)


import sys

exec(sys.stdin.read())

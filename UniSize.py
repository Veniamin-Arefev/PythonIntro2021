def sizer(cls):
    class Size:
        def __get__(self, instance, owner):
            func = getattr(instance, "__len__", None)
            if func is None:
                func = getattr(instance, "__abs__", None)
            return 0 if func is None else func()

    cls.size = Size()
    return cls


import sys

exec(sys.stdin.read())

def dec(self, fun):
    def wrap(*x):
        self.__name = fun.__name__
        return DivStr(result) if type(result := fun(self, *x)) == str else result

    return wrap


class DivStr(str):
    def __init__(self, string):
        super().__init__()
        for name, fun in str.__dict__.items():
            if callable(fun) and not name.startswith("__"):
                self.__dict__[name] = dec(self, fun)
                setattr(self.__dict__[name], "__name__", name)

    def __floordiv__(self, other):
        return [DivStr(self[i * (leen := len(self) // int(other)):(i + 1) * leen]) for i in range(int(other))]

    def __mod__(self, other):
        return DivStr(self[-(len(self) % int(other)):]) if other != 1 else DivStr("")

    def __getitem__(self, item):
        return DivStr(result) if type(result := super(DivStr, self).__getitem__(item)) == str else result

    def __add__(self, other):
        return DivStr(result) if type(result := super(DivStr, self).__add__(other)) == str else result

    def __mul__(self, other):
        return DivStr(result) if type(result := super(DivStr, self).__mul__(other)) == str else result

    def __rmul__(self, other):
        return DivStr(result) if type(result := super(DivStr, self).__rmul__(other)) == str else result


import sys

exec(sys.stdin.read())

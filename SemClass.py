from collections import defaultdict


class Lock:
    semaphores = defaultdict(int)

    def __get__(self, instance, owner):
        if (ins_id := type(self).semaphores[getattr(instance, "__sem", None)]) == 0 or ins_id == id(instance):
            type(self).semaphores[getattr(instance, "__sem", None)] = id(instance)
            return getattr(instance, "__sem", None)
        else:
            return None

    def __set__(self, instance, value):
        if getattr(instance, "__sem", None) is not None:
            type(self).semaphores[getattr(instance, "__sem", None)] = 0
        setattr(instance, "__sem", value)

    def __delete__(self, instance):
        if type(self).semaphores[getattr(instance, "__sem", None)] == id(instance):
            type(self).semaphores[getattr(instance, "__sem", None)] = 0
        pass

    @staticmethod
    def locked(cls):
        class New_Class(cls):
            lock = Lock()

            def __del__(self):
                del self.lock
                if getattr(super(), "__del__", None) is not None:
                    super().__del__()

        return New_Class


import sys

exec(sys.stdin.read())

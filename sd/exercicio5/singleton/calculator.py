from threading import Lock

class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Calculator(metaclass=SingletonMeta):
    def sum(self, x, y):
        return x + y

    def sub(self, x, y):
        if x < 0 or y < 0:
            return x + y
        return x - y
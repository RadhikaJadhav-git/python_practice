from threading import Lock

class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def connect(self):
        return "Connected to DB"


# Usage
db1 = Database()
db2 = Database()

print(db1 is db2)  # True

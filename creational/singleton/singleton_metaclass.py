

class SingletonMetaClass(type):
    # static variable _instance
    _instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Config(metaclass=SingletonMetaClass):

    def __init__(self):
        self.__dict__ = {
            'DB': 'localhost',
            'user': 'root'
        }

    def __str__(self):
        return f"<{self.__class__.__name__} {id(self)}>"

class DBConn(metaclass=SingletonMetaClass):
    def get_config(self):
        return {
            'query': NotImplementedError()
        }


if __name__ == '__main__':
    o1 = Config()
    o2 = Config()
    d1, d2 = DBConn(), DBConn()
    print('Config IDS: ', *map(id, [o1,o2]))
    print('DBConn IDS: ', *map(id, [d1,d2]))
    assert id(o1) == id(o2), "Config different Instances" 
    assert id(d1) == id(d2), "DBConn different Instances" 
    assert id(o1) != id(d1), "Config and DBConn should be different"

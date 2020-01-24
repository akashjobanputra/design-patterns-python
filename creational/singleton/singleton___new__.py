
class Config():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_config'):
            cls._config = super(Config, cls).__new__(cls, *args, **kwargs)
        return cls._config

    def __init__(self):
        self.DB_URL = 'localhost'
        self.DB_USER = 'root'
        self.DB_PSWD = 'root'

    def __str__(self):
        return f"<{self.__class__.__name__}: {id(self)}>"

class DBConn():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_conn'):
            cls._conn = super(DBConn, cls).__new__(cls, *args, **kwargs)    # CHeck what super().__new__ does
        return cls._conn

    def __init__(self):
        # __new__ always returns an appropriate object, so __init__ is always called - even if the instance already exists
        # Check how many times __init__ is called by adding a counter in static.
        self.conn = NotImplementedError()

    def __str__(self):
        return f"<{self.__class__.__name__}: {id(self)}>"


if __name__ == '__main__':
    o1 = Config()
    o2 = Config()
    d1, d2 = DBConn(), DBConn()
    print('Config IDS: ', *[o1,o2])
    print('DBConn IDS: ', *[d1,d2])
    assert id(o1) == id(o2), "Config different Instances" 
    assert id(d1) == id(d2), "DBConn different Instances" 
    assert id(o1) != id(d1), "Config and DBConn should be different"

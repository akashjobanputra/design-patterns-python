class Config:
    _instance = None
    class _Config():
        def __init__(self):
            self.DB_URL = 'localhost'
            self.DB_USER = 'root'
            self.DB_PSWD = 'root'

    @classmethod
    def get_config(cls):
        if not cls._instance:
            cls._instance = cls._Config()
        return cls._instance

if __name__ == '__main__':
    o1 = Config().get_config()
    o2 = Config().get_config()
    # d1, d2 = DBConn(), DBConn()
    print('Config IDS: ', *map(id, [o1,o2]))
    # print('DBConn IDS: ', *[d1,d2])
    assert id(o1) == id(o2), "Config different Instances" 
    # assert id(d1) == id(d2), "DBConn different Instances" 
    # assert id(o1) != id(d1), "Config and DBConn should be different"

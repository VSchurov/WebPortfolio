class Config(object):
    """Base config for staging cluster"""
    TESTING = False
    DB_SERVER = '192.168.1.228'

    @property
    def DATABASE_URI(self):  #Note: all caps
        return f"mysql://user@{self.DB_SERVER}/staging.db"


class ProductionConfig(Config):
    DATABASE_URI = 'postgresql://ivan@localhost/heap.db'


class DevelopmentConfig(Config):
    DATABASE_URI = 'sqlite:///databases/dev_db.db'


class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///databases/test.db'

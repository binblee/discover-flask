import os


class BaseConfig():
    DEBUG = False
    SECRET_KEY = b'\xb0\x12g]\x91#>\x1d9\x83S|d\xec\x8e\x1b\x13R./\xd9\x85\xe3O'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
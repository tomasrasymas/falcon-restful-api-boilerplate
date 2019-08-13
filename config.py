import os


class Config:
    DATABASE_URL = 'sqlite:///sample.db'


class DevelopmentConfig(Config):
    pass


class TestConfig(Config):
    pass


class ProductionConfig(Config):
    pass


def get_config():
    env = os.environ.get('env', None)

    if env == 'development':
        return DevelopmentConfig
    elif env == 'production':
        return ProductionConfig
    elif env == 'test':
        return TestConfig
    else:
        return DevelopmentConfig


config = get_config()

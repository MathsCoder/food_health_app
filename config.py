import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base config, uses staging database server."""

    FLASK_ENV = "development"
    TESTING = False
    DEBUG = False
    SECRET_KEY = "BAD_KEY"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASEDIR, "app.sqlite")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True

    # load environment variables
    # dotenv_path = os.path.join(BASEDIR, '.env')
    # load_dotenv(dotenv_path)


class ProductionConfig(Config):
    """Uses production database server."""

    FLASK_ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASEDIR, "test.sqlite")}'
    WTF_CSRF_ENABLED = False

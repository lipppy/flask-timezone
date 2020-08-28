import os

APP_ROOT = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    APP_NAME = 'App Name'
    PAGE_TITLE = "Page Title"
    SECRET_KEY = 'TiszteltHolgyeimEsUraimTiszteltElnokUrBoldogKaracsonyt'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PG_DB_HOST = "pg_db_host" #localhost
    PG_DB_PORT = "pg_db_port" # 5432
    PG_DB_NAME = "pg_db_name"
    PG_DB_USERNAME = "pg_db_username" # postgres
    PG_DB_PASSWORD = "pg_db_password"

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
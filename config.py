import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATEBASE_URI')
    SECRET_KEY = 'MWYyZDFlMmU2N2Rm'

    SECURITY_PASSWORD_SALT = 'mysalt18'
    SECURITY_PASSWORD_HASH = 'bcrypt'


class ProductionConfig(Config):
    DEBUG = False

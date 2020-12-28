#config variables

import os
from decouple import config

BASE_DIR=os.path.dirname(os.path.realpath(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='f90abf5a336b9b9bb5e92f4a'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI=config('DEV_DATABASE_URI')
   # SQLALCHEMY_ECHO=True
    DEBUG=True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR,'test.db')
    SQLALCHEMY_ECHO=True
    DEBUG=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=config('DATABASE_URI')
    DEBUG=True
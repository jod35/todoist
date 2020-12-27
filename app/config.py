#config variables

import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

print(BASE_DIR)

class Config:
    pass

class DevConfig(Config):
    pass

class TestConfig(Config):
    pass

class ProdConfig(Config):
    pass
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or  "aoiasfljnabrnonj43er2"

    MONGODB_SETTINGS = { 'db' : 'YOGA_Studio'}

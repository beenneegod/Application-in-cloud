#Project created by:
#           Serhii Burenkov
#           Dmytro Tvedovskyi
#           Rostyslav Pyrozhenko
# for class: Interned applications created in cloud 


import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'memcached'
    SECRET_KEY = 'key'
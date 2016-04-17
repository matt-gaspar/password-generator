import os

class Config(object):
    DEBUG = os.getenv('DEBUG', False)
    SECRET_KEY = os.getenv('SECRET_KEY','123456reallysecretkey')
    EXCLUDE_CHARS = ["$","'","`"]

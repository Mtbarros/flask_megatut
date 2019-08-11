import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    APPLICATION_ROOT = "/~ist176165/cgi-bin/flask_megatut/main.cgi"

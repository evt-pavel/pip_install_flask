import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__)) # эта переменная - путь к папке с запускаемым скриптом
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # второй вариант создания переменной SECRET_KEY['SECRET_KEY'] = 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['email@email.com']
    POSTS_PER_PAGE = 5

    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir,
                                                          'app.db') + '?check_same_thread=False&confirm_deleted_rows=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

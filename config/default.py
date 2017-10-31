# -*- coding: utf-8 -*-
"""Default configuration file. We check for SECRET_KEY,
DATABASE_PASSWORD and DATABASE_HOST on the environment. These values are
also set in instance/config.py.
To run this example, you will need to put those values in a config.py
file in the instance folder, or create a start up scrip where you export
these values and then start the application.
For example::

    $ export DATABASE_PASSWORD='my-database-password'
    $ export DATABASE_HOST="my-database-server"
    $ export FLASK_CONFIG="development" # or test, production, ...

    $ python manage.py

"""
import os

class Config:
    """Basic Flask settings."""
    DEBUG=False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'myspecialsecretkey'

    """ OTRS Settings """
    DATABASE_NAME = 'otrs'
    DATABASE_USER = 'otrs'
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') or ""
    DATABASE_HOST = os.environ.get('DATABASE_HOST') or ""
    DATABASE_PORT = 5432


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    """Database path."""
    BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
    DATABASE = os.path.join(BASEDIR,"data","temp.db")


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    """Database path."""
    BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
    DATABASE = os.path.join(BASEDIR,"data","temp.db")
    

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
"""dictionary: Different configuration settings."""

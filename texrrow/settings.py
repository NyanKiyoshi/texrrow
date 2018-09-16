import os.path
import posixpath
from ast import literal_eval
from os import getenv

APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
WEBPACK_MANIFEST_PATH = os.path.abspath(
    os.path.join(PROJECT_ROOT, 'webpack-bundle.json'))


def _make_sqlite_db_path():
    database_url = 'sqlite:///' + posixpath.join(PROJECT_ROOT, 'db.sqlite')
    return database_url


def getenv_ast(name, default_value):
    if name in os.environ:
        value = os.environ[name]
        try:
            return literal_eval(value)
        except ValueError as e:
            raise ValueError(
                '{} is an invalid value for {}'.format(value, name)) from e
    return default_value


DEBUG = getenv_ast('DEBUG', True)
SECRET_KEY = getenv('SECRET_KEY')
CSRF_SECRET = getenv('SECRET_KEY', SECRET_KEY)

TEMPLATE_FOLDER = os.path.join(PROJECT_ROOT, 'templates')

LANGUAGES = 'EN', 'FR'
BABEL_DEFAULT_LOCALE = 'EN'
BABEL_DEFAULT_TIMEZONE = 'UTC'

WTF_CSRF_ENABLED = False

ENABLE_DEBUG_TOOLBAR = False
DEBUG_TB_INTERCEPT_REDIRECTS = getenv_ast(
    'DEBUG_TB_INTERCEPT_REDIRECTS', False)

NEXT_SLIDE_KEY = 'right'  # right arrow
PREV_SLIDE_KEY = 'left'  # left arrow

SQLALCHEMY_MIGRATE_REPO = os.path.join(PROJECT_ROOT, 'db_repository')
SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
if not SQLALCHEMY_DATABASE_URI:
    SQLALCHEMY_DATABASE_URI = _make_sqlite_db_path()

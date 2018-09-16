import os.path

from texrrow.core.utils.environ import getenv, getenv_bool

APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
WEBPACK_MANIFEST_PATH = os.path.abspath(
    os.path.join(PROJECT_ROOT, 'webpack-bundle.json'))

DEBUG = getenv_bool('DEBUG', True)
SECRET_KEY = getenv('SECRET_KEY', 'secret')
CSRF_SECRET = getenv('SECRET_KEY', SECRET_KEY)

TEMPLATE_FOLDER = os.path.join(PROJECT_ROOT, 'templates')

LANGUAGES = 'EN', 'FR'
BABEL_DEFAULT_LOCALE = 'EN'
BABEL_DEFAULT_TIMEZONE = 'UTC'

WTF_CSRF_ENABLED = False

ENABLE_DEBUG_TOOLBAR = getenv_bool('ENABLE_DEBUG_TOOLBAR', False)
DEBUG_TB_INTERCEPT_REDIRECTS = getenv_bool(
    'DEBUG_TB_INTERCEPT_REDIRECTS', False)

NEXT_SLIDE_KEY = 'right'  # right arrow
PREV_SLIDE_KEY = 'left'  # left arrow

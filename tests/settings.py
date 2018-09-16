from texrrow.settings import *  # noqa

TESTING = True
SERVER_NAME = 'localhost.test'  # RFC2606

SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL', 'sqlite:///:memory:')

SECRET_KEY = 'test'
WTF_CSRF_ENABLED = False

PASSWORD_CONFIG = {'pbkdf2_sha512__default_rounds': 1}
ENABLE_DEBUG_TOOLBAR = False

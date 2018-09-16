from six import raise_from
from os import environ

E_INVALID_BOOL = '%r is an invalid boolean value.'


def getenv_or_raise(name, error_message):
    try:
        return environ[name]
    except KeyError as exc:
        exc_value = KeyError(error_message)
        raise_from(exc_value, exc)
        raise exc_value


def getenv_int(name, default=None):
    if name in environ:
        return int(environ[name])
    return default


def getenv_bool(name, default=None):
    if name in environ:
        value = environ[name].lower()
        if value == 'false':
            return False
        elif value == 'true':
            return True
        else:
            raise ValueError(E_INVALID_BOOL % value)
    return default


def getenv(name, default=None):
    if name in environ:
        return environ[name]
    return default


__all__ = 'getenv_or_raise', 'getenv_int', 'getenv_bool', 'getenv'

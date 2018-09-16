from unittest import mock

import pytest

from texrrow.core.utils import environ


@pytest.fixture
def mocked_environ():
    """Mocks the imported os.environ with a mutable dict."""
    default_env = {'dummy': 'yes'}
    with mock.patch.object(
            environ, 'environ', create=True, new=default_env) as mocked:
        yield mocked


def test_getenv(mocked_environ):
    """Test `getenv` has the expected behaviors:
        1. Retrieve the value if existing;
        2. Returns the default value (None or given one)."""
    assert environ.getenv('dummy') == 'yes'
    assert environ.getenv('invalid') is None
    assert environ.getenv('invalid', 'abc') == 'abc'


def test_getenv_or_raise(mocked_environ):
    """Test `getenv_or_raise()` with an existing key."""
    assert environ.getenv_or_raise('dummy', None) == 'yes'


def test_getenv_or_raise__missing_value(mocked_environ):
    """Test `getenv_or_raise()` with a non-existing key,
    which should raise a KeyError exception with the given message."""
    error_message = 'Oopsie.'
    with pytest.raises(KeyError, message=error_message):
        environ.getenv_or_raise('invalid', error_message)


def test_getenv_int(mocked_environ):
    """Test `getenv_int()` with valid values.
    1. Should be able to parse a valid integer string to an integer;
    2. Should return the default given value is the key is non-existing."""
    mocked_environ['number'] = '12'
    assert environ.getenv_int('number') == 12
    assert environ.getenv_int('invalid', 123) == 123


def test_getenv_int__invalid_value(mocked_environ):
    """Test `getenv_int()` with an invalid integer value,
    which should raise an error."""
    with pytest.raises(
            ValueError,
            message='invalid literal for int() with base 10: \'yes\''):
        environ.getenv_int('dummy')


@pytest.mark.parametrize('value,expected_result', (
    ('true', True),
    ('True', True),
    ('false', False),
    ('False', False)))
def test_getenv_bool(mocked_environ, value, expected_result):
    """Test `getenv_bool()` with valid values."""
    mocked_environ['boolean'] = value
    assert environ.getenv_bool('boolean') == expected_result


def test_getenv_bool__default_value(mocked_environ):
    """Test `getenv_bool()` with an invalid boolean value,
    which should raise an error."""
    assert environ.getenv_bool('invalid') is None
    assert environ.getenv_bool('invalid', False) is False


def test_getenv_bool__invalid_value(mocked_environ):
    """Test `getenv_bool()` with an invalid boolean value,
    which should raise an error."""
    with pytest.raises(ValueError, message=environ.E_INVALID_BOOL % 'yes'):
        environ.getenv_bool('dummy')

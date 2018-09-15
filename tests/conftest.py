from os.path import dirname, join, realpath
from unittest import mock

import pytest
from flask import url_for
from sqlalchemy_utils import create_database, database_exists, drop_database

from texrrow.application import create_app, db
from texrrow.core.commands import populatedb

from .settings import SQLALCHEMY_DATABASE_URI


@pytest.fixture(scope='session')
def app():
    config_path = join(realpath(dirname(__file__)), 'settings.py')
    with mock.patch(
            'texrrow.application.get_config_path') as mocked_cfg_path:
        mocked_cfg_path.return_value = config_path
        flask_app = create_app()
        mocked_cfg_path.assert_called_once_with()

    # make jinja raise an exception on undefined variables
    # FIXME: we need to fix the bootstrap-wtf
    # flask_app.jinja_env.undefined = StrictUndefined()

    return flask_app


@pytest.fixture
def pushed_app(app):
    app_context = app.app_context()
    app_context.push()

    yield app
    app_context.pop()


@pytest.fixture(scope='session', autouse=True)
def database(app):
    engine = db.create_engine(SQLALCHEMY_DATABASE_URI)

    # do nothing if the database is in memory,
    # as it's not correctly handling it
    if str(engine.url).endswith(':memory:'):
        yield
        return

    if database_exists(engine.url):
        drop_database(engine.url)

    create_database(engine.url)
    yield

    drop_database(SQLALCHEMY_DATABASE_URI)


@pytest.fixture(scope='function')
def empty_db(app, pushed_app):
    db.drop_all()
    db.create_all()
    return db


@pytest.fixture(scope='function')
def initial_data(empty_db):
    populatedb.run()
    return db


@pytest.fixture
def staff_user(empty_db):
    return populatedb.create_staff_user()[0]


@pytest.fixture
def client(pushed_app):
    return pushed_app.test_client()


@pytest.fixture
def authorized_client(client, staff_user):
    # FIXME: we should not use the view directly
    client.post(
        url_for('dashboard.login'),
        data={'email': staff_user.email, 'password': 'admin'})
    return client

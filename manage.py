#!/usr/bin/env python

import os

import click
from flask.cli import FlaskGroup, with_appcontext
from flask_migrate.cli import db as db_group

from texrrow.application import create_app
from texrrow.core.commands import populatedb

os.environ.setdefault('FLASK_ENV', 'development')


@click.group(cls=FlaskGroup, create_app=create_app)
def manager():
    """Management script for the flask application."""


@db_group.command(name='populate')
@with_appcontext
def db_populate():
    """Populate a database with example data."""
    populatedb.run()


@manager.group()
def translate():
    """Translation and localization commands."""


@translate.command(name='update')
def translate_update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.pot -d translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')


@translate.command(name='compile')
@with_appcontext
def translate_compile():
    """Compile all languages."""
    if os.system('pybabel compile -d translations'):
        raise RuntimeError('compile command failed')


@translate.command(name='init')
@click.argument('lang')
def translate_init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
            'pybabel init -i messages.pot -d translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')


if __name__ == '__main__':
    manager()

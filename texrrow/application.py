import os.path

import jinja2

from flask_babel import pgettext
from flask_wtf.csrf import generate_csrf

from .core.extensions import app, babel, bootstrap, csrf
from .core.views import *  # noqa
from .sendkeys.views import sendkeys_bp

LOGIN_VIEW = '.login'


def get_config_path():
    config_filename = os.getenv('CONFIG_FILENAME', 'settings.py')
    app_dir_path = os.path.realpath(os.path.dirname(__file__))
    config_path = os.path.join(app_dir_path, config_filename)
    return config_path


def create_app():
    # retrieve the settings file to setup flask
    app.config.from_pyfile(get_config_path())
    app.root_path = app.config['PROJECT_ROOT']

    # configure extensions
    configure_extensions()
    return app


def configure_extensions():
    configure_jinja()

    register_extensions()
    register_blueprints()

    install_debug_toolbar()


def configure_jinja():
    """This:
     - configures jinja's policy on undefined variables;
     - install any globals needed by the templates;
     - install any extensions used by the templates."""
    # Configure jinja to warn undefined variables.
    # For more information and possibilities, see:
    #     http://jinja.pocoo.org/docs/2.10/api/#jinja2.make_logging_undefined
    undefined_logger = jinja2.make_logging_undefined(
        app.logger, base=jinja2.Undefined)
    app.jinja_env.undefined = undefined_logger

    # install pgettext for i18n and generate_csrf for non-standard forms
    app.jinja_env.globals['pgettext'] = pgettext
    app.jinja_env.globals['generate_csrf'] = generate_csrf


def install_debug_toolbar():
    """This will load and enable flask-debugtoolbar
    if the app is in debug mode (development)
    but will not if it's running the tests."""
    if app.debug and not app.testing and app.config['ENABLE_DEBUG_TOOLBAR']:
        from flask_debugtoolbar import DebugToolbarExtension
        DebugToolbarExtension(app)


def register_extensions():
    """Setup every flask extensions used by this project."""
    babel.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)


def register_blueprints():
    """Register the project blueprints.
    This will be dropped in the future for an import level registering
    to remove any back dependencies."""
    app.register_blueprint(sendkeys_bp)


if __name__ == '__main__':
    create_app().run()

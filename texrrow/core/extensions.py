# -*- coding: utf-8 -*-
from flask import Flask
from flask_babel import Babel
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
babel = Babel(configure_jinja=False)
bootstrap = Bootstrap()
csrf = CSRFProtect()
login_manager = LoginManager()

app = Flask('texrrow')

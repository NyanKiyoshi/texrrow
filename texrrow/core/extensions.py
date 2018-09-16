# -*- coding: utf-8 -*-
from flask import Flask
from flask_babel import Babel
from flask_wtf import CSRFProtect

from flask_bootstrap import Bootstrap

babel = Babel(configure_jinja=False)
bootstrap = Bootstrap()
csrf = CSRFProtect()

app = Flask('texrrow')

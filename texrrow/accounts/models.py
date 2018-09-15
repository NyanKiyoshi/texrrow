from datetime import datetime

from flask import current_app
from sqlalchemy_utils import EmailType, PasswordType

from ..core.database import Model, SurrogatePK
from ..core.extensions import db

DEFAULT_PASSWORD_CONFIG = {'schemes': ['pbkdf2_sha512']}
MAX_EMAIL_LENGTH = 255


def _get_password_config(**kwargs):
    additional_config = current_app.config.get('PASSWORD_CONFIG')
    kwargs.update(DEFAULT_PASSWORD_CONFIG)
    if additional_config:
        kwargs.update(additional_config)
    return kwargs


class Account(SurrogatePK, Model):
    __tablename__ = 'accounts'
    _picture = None

    email = db.Column(EmailType(MAX_EMAIL_LENGTH), nullable=False, unique=True)
    password = db.Column(
        PasswordType(onload=_get_password_config), nullable=False)

    creation_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    is_active = db.Column(db.Boolean, default=True)
    is_staff = db.Column(db.Boolean, default=True)
    is_superuser = db.Column(db.Boolean, default=False)

    def check_password(self, guest):
        return self.password == guest

    @property
    def can_login(self):
        return self.is_active and self.is_staff

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return self.email

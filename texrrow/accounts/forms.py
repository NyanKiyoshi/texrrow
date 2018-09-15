from flask_babel import lazy_pgettext
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField
from wtforms.validators import Length, Required
from wtforms_components.fields import EmailField

from ..accounts.models import MAX_EMAIL_LENGTH, Account

E_INVALID_CREDENTIALS = lazy_pgettext(
    'Dashboard login: invalid email or password', 'Invalid email or password.')
L_EMAIL = lazy_pgettext('Dashboard login form label', 'Email')
L_PASSWORD = lazy_pgettext('Dashboard login form label', 'Password')


class LoginForm(FlaskForm):
    email = EmailField(
        L_EMAIL, validators=[Required(), Length(-1, MAX_EMAIL_LENGTH)])
    password = PasswordField(L_PASSWORD, validators=[Required()])

    def check_credentials(self):
        account = Account.filter_by(email=self.email.data).first()
        if (account and
                account.can_login and
                account.check_password(self.password.data)):
            return account
        self.errors['__form__'] = [E_INVALID_CREDENTIALS]

    def is_valid(self):
        if self.validate_on_submit():
            return self.check_credentials()
        return

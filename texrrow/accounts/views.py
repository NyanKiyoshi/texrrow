from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_babel import lazy_pgettext
from flask_login import login_user, logout_user

from ..utils.http import escape_urn
from .forms import LoginForm

MSG_LOGGED_IN = lazy_pgettext(
    'Dashboard login flash message', 'Logged in successfully.')

MSG_LOGGED_OUT = lazy_pgettext(
    'Dashboard login flash message', 'You have been logged out.')


account_bp = Blueprint(
    url_prefix='/accounts', name='account', import_name=__name__)


@account_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    account = form.is_valid()
    if account:
        login_user(account)
        flash(MSG_LOGGED_IN)
        next_url = request.args.get('next')
        if next_url:
            next_url = escape_urn(next_url)
        return redirect(next_url or url_for('.index'))
    return render_template('login.html', form=form)


@account_bp.route('/logout')
def logout():
    logout_user()
    flash(MSG_LOGGED_OUT)
    return redirect(url_for('account.login'))

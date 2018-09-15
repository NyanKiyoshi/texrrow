from ...accounts.models import Account
from ...application import app


def create_staff_user():
    attrs = {
        'email': 'staff@example.com',
        'password': 'admin',
        'is_staff': True}
    account = Account.filter_by(email=attrs['email']).first()
    created = account is None

    if created:
        account = Account.create(**attrs)

    return account, created


def run():
    account, created = create_staff_user()
    if created:
        app.logger.info('Created staff account: %s' % account.email)

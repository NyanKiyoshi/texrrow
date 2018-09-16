import pytest
from unittest import mock
from flask import url_for

from .settings import NEXT_SLIDE_KEY, PREV_SLIDE_KEY


@mock.patch('keyboard.send')
@pytest.mark.parametrize('endpoint, expected_call', (
    ('next', (NEXT_SLIDE_KEY,)),
    ('prev', (PREV_SLIDE_KEY,))))
def test_change_slide(mocked_send, endpoint, expected_call, client):
    post_url = url_for('sendkeys.%s' % endpoint)
    client.post(post_url)
    mocked_send.assert_called_once_with(*expected_call)

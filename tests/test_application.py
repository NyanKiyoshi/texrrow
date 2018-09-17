import mock
from texrrow import application


@mock.patch('flask_debugtoolbar.DebugToolbarExtension')
def test_install_debug_toolbar(mocked_install):
    application.install_debug_toolbar()
    assert mocked_install.call_count == 0

    with mock.patch.object(application, 'app') as mocked_app:
        mocked_app.config['ENABLE_DEBUG_TOOLBAR'] = True
        application.install_debug_toolbar()
        assert mocked_install.call_count == 1


def test_get_config_path():
    assert application.get_config_path().endswith('settings.py')

import os
import os.path
import sys

PORT = 5000
UWSGI_PATH = os.path.realpath(os.path.join(sys.executable, os.pardir, 'uwsgi'))


def _get_port_from_argv():
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        return port
    return PORT


def start_flask():
    from .application import create_app
    create_app().run(host='0.0.0.0', port=_get_port_from_argv(), debug=False)


def start_uwsgi():
    port = ':%d' % _get_port_from_argv()
    argv = ['uwsgi', '--http', port, '--module', 'texrrow.wsgi:application']
    os.execve(UWSGI_PATH, argv, os.environ)

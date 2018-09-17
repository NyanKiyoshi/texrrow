"""We want to ensure that users can run Texrrow through UWSGI without issues.
This script is ran by Travis and AppVeyor to ensure the compatibility.

This is a heavy test and incompatible test with pytest.
Thus we keep it separated from the rest of the tests."""
import os
import signal
import sys
import time

import mock
import requests
import requests.exceptions

from texrrow import __main__ as main

TEST_PORT = 12345


def _knock_url_and_wait(url, timeout_per_request=1, global_timeout=10):
    status = None
    end_time = time.time() + global_timeout
    while status is None:
        try:
            response = requests.head(url, timeout=timeout_per_request)
            status = response.status_code
        except requests.exceptions.ConnectionError:  # noqa
            if time.time() > end_time:
                raise
    assert status == 200


def _run_and_test(to_run):
    child_pid = os.fork()
    if child_pid == 0:
        to_run()
        sys.exit(0)
    try:
        test_url = 'http://127.0.0.1:%d' % TEST_PORT
        time.sleep(0.1)
        pid, status = os.waitpid(child_pid, os.P_NOWAIT)

        # ensure the process did not exit
        assert not os.WEXITSTATUS(pid)

        # try to ping uwsgi and get a HTTP 200
        _knock_url_and_wait(test_url)
    finally:
        os.kill(child_pid, signal.SIGTERM)
        os.wait()


@mock.patch.object(main, 'PORT', new=TEST_PORT)
def test_start_servers():
    _run_and_test(main.start_uwsgi)
    _run_and_test(main.start_flask)


if __name__ == '__main__':
    test_start_servers()

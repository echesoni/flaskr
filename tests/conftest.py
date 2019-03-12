import os
import tempfile

import pytest
import flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('uft8')

@pytest.fixture
def app():
    # Create and opens a tempfile,
    # and override db path to point to temp path
    db_fd, db_path = tempfile.mkstemp()

    # TESTING tells Flask app is in testing mode
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yeild app

    # Close and remove tempfile
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    # Tests will use client to make requests to apps
    # without running server
    return app.test_client()


@pytest.fixture
def runner(app):
    # Creates a runner that can call Click commands
    # registered with the app
    return app.test_cli_runner


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )
    def logout(self):
        return self._client.get('/auth/logout')

@pytest.fixture
def auth(client):
    return AuthActions(client)

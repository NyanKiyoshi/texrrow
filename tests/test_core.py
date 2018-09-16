from flask import url_for


def test_index(client):
    response = client.get(url_for('index'))
    assert response.status_code == 200

import pytest
from chalice.config import Config
from chalice.local import LocalGateway
from app import app


@pytest.fixture()
def client():
    return LocalGateway(app, Config())


def test_app_int(client):
    response = client.handle_request(method='GET', path='/', headers={}, body='')
    assert response['statusCode'] == 200
    assert 'origin' in response['body']
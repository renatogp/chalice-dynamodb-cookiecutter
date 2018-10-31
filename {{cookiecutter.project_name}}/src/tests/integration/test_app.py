import pytest
from app import app


def test_app_int(client):
    response = client.get(path='/')
    assert response['statusCode'] == 200
    assert 'origin' in response['body']
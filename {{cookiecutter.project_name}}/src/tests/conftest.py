import json
import os
import random
import uuid

import pytest
import vcr as base_vcr
from chalice.config import Config
from chalice.local import LocalGateway

from app import app


@pytest.fixture()
def vcr_context():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return base_vcr.VCR(
        ignore_localhost=True,
        ignore_hosts=['169.254.170.2'],
        serializer='yaml',
        cassette_library_dir=os.path.join(current_dir, 'integration/cassettes'),
        record_mode='once',
    )

class TestHttpClient(object):
    def __init__(self, app_local_gateway):
        self.app_local_gateway = app_local_gateway

    def get(self, path):
        return self.app_local_gateway.handle_request(
            method='GET', 
            path=path,
            headers={
                'Content-Type': 'application/json',
            },  
            body='',
        )

    def post(self, path, data=None):
        return self.app_local_gateway.handle_request(
            method='POST', 
            path=path,
            headers={
                'Content-Type': 'application/json',
            },  
            body=json.dumps(data) if data else '',
        )

    def put(self, path, data=None):
        return self.app_local_gateway.handle_request(
            method='PUT', 
            path=path,
            headers={
                'Content-Type': 'application/json',
            },  
            body=json.dumps(data) if data else '',
        )


@pytest.fixture()
def app_local_gateway():
    return LocalGateway(app, Config())


@pytest.fixture()
def client(app_local_gateway):
    return TestHttpClient(app_local_gateway)


@pytest.fixture
def create_event():
    def create_event_inner(uri, method, path, content_type='application/json'):
        return {
            'requestContext': {
                'httpMethod': method,
                'resourcePath': uri,
            },
            'headers': {
                'Content-Type': content_type,
            },
            'pathParameters': path,
            'queryStringParameters': {},
            'body': '',
            'stageVariables': {},
        }
    return create_event_inner
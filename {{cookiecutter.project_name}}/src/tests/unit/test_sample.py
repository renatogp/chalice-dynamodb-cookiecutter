import os
import json

import vcr
import app

CASSETTE_LIBRARY_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures/')

@vcr.use_cassette(cassette_library_dir=CASSETTE_LIBRARY_DIR, ignore_localhost=True)
def test_sample(create_event):
    event = create_event('/', 'GET', {})
    response = app.app(event, context=None)
    
    assert response['statusCode'] == 200
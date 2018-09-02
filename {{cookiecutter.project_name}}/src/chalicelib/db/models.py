import os
import uuid

from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model

from chalicelib import get_stage

def generate_uuid():
    return str(uuid.uuid4())


class SampleModel(Model):
    uuid = UnicodeAttribute(hash_key=True, default=generate_uuid)
    name = UnicodeAttribute(null=True)

    class Meta:
        table_name = '{}-sample'.format(get_stage())

        if 'DYNAMODB_HOST' in os.environ:
            host = os.environ['DYNAMODB_HOST']

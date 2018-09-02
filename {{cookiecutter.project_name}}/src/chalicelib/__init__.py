import os

STAGE_NAME_ENV_KEY = 'STAGE_NAME'

def get_stage():
    return os.environ.get(STAGE_NAME_ENV_KEY, 'undefined-stage')
import os

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Development')

SECS_TO_YEARS = 60 * 60 * 24 * 31 * 12

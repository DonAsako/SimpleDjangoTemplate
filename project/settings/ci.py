"""
Continuous-integration settings.

Used to run the test suite in CI.
"""

from .base import *  # noqa: F403

DEBUG = False

# Fast, insecure hashing — fine for throwaway CI databases.
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}},
    'root': {'handlers': ['console'], 'level': 'WARNING'},
}

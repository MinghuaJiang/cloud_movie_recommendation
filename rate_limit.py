from flask_limiter import Limiter
from flask import request
from flask_limiter.util import get_remote_address


def limit_function():
    key = 'rate-limit/%s/%s/' % (request.endpoint, get_remote_address())
    return key


def get_limiter(app):
    limiter = Limiter(
        app,
        key_func=limit_function,
        global_limits=["200 per day", "50 per hour"]
    )
    return limiter


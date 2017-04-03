import logging
from flask import Flask, request
import rate_limit


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

application = Flask(__name__)

limiter = rate_limit.get_limiter(application)


@application.route('/rate-limited')
@limiter.limit("10 per hour")
def test():
    return "this is rate limit test"


@application.route('/')
@limiter.exempt
def index():
    return "hello world!"


@application.route('/rate')
@limiter.limit("5 per hour")
def rate():
    return "test"

if __name__ == '__main__':
	application.debug = True
	application.run()
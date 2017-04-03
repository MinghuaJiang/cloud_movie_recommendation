import logging
from flask import Flask, request
import rate_limit_redis


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

application = Flask(__name__)


@application.route('/rate-limited')
@rate_limit_redis.ratelimit(limit=10, per=60*1)
def test():
    return "this is a rate limit test"

@application.route('/rate-limited2')
@rate_limit_redis.ratelimit(limit=15, per=60*1)
def test2():
    return "this is a rate limit test2"

@application.route('/')
def hello():
    return "hello world"

if __name__ == '__main__':
	application.debug = True
	application.run()
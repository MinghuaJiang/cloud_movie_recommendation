import json
import urllib2

host_root = "http://13.58.38.231:5000"


def get_movie_detail(user_id, movie_id):
    result = json.load(urllib2.urlopen(host_root + "/api/v1/movie/" + user_id + "/" + str(movie_id)))
    return json.dumps(result)


def get_paging_genre_movies(genre, page):
    result = json.load(urllib2.urlopen(host_root + "/api/v1/movie/genre/" + genre + "/" + str(page)))
    return json.dumps(result)


def get_personalized_recommendation(userid, count):
    result = json.load(urllib2.urlopen(host_root + "/api/v1/recommendation/" + userid + "/" + str(count)))
    return json.dumps(result)


def get_most_popular(count):
    result = json.load(urllib2.urlopen(host_root + "/api/v1/recommendation/popular/" + str(count)))
    return json.dumps(result)


def get_top_rated(count):
    result = json.load(urllib2.urlopen(host_root + "/api/v1/recommendation/rating/" + str(count)))
    return json.dumps(result)


def get_rated_count(user_id):
    result = json.load(urllib2.urlopen(host_root + "/api/v1/rating/" + user_id))
    return json.dumps(result)


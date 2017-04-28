import json


def search(query):
    result = dict()
    result["json"] = [{'movie_name': 'Test', 'movie_small_url': 'Test'},
                      {'movie_name': 'Test', 'movie_small_url': 'Test'}]
    return json.dumps(result)


def detail(movie_id):
    result = dict()
    result["detail"] = {'movie_name': 'Test', 'movie_average_rating': 4.5, 'vote_count': 100,
                        'genre': ['Action', 'Love'], 'introduction': "", 'image_url': '', 'youtube_url': ''}
    result['comment'] = {'comment': '', 'rating': '', 'comment_by': '', 'comment_time': ''}
    result['comments'] = [{'comment': '', 'rating': '', 'comment_by': '', 'comment_time': ''}]
    return json.dumps(result)


def get_most_popular_movies():
    result = dict()
    result["movie"] = [{'movie_id': '', 'movie_name': '', 'movie_url': ''},
                       {'movie_id': '', 'movie_name': '', 'movie_url': ''}]
    return json.dumps(result)


def get_paging_most_popular_movies(page):
    result = dict()
    return json.dumps(result)


def get_top_rated_movies():
    result = dict()
    return json.dumps(result)


def get_paging_top_rated_movies(page):
    result = dict()
    return json.dumps(result)


def get_paging_genre_movies(page):
    result = dict()
    return json.dumps(result)


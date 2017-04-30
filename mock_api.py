import json


def search(query):
    result = dict()
    result["json"] = [{'movie_name': 'Test', 'movie_small_url': 'Test'},
                      {'movie_name': 'Test', 'movie_small_url': 'Test'}]
    return json.dumps(result)


def detail(movie_id):
    result = dict()
    result["detail"] = {
        'movie_name': 'Name',
        'movie_average_rating': 4.5,
        'vote_count': 100,
        'genre': ['Action', 'Love'],
        'introduction': "With the impending ice age almost upon them, a mismatched trio of prehistoric critters – Manny the woolly mammoth, Diego the saber-toothed tiger and Sid the giant sloth – find an orphaned infant and decide to return it to its human parents. Along the way, the unlikely allies become friends but, when enemies attack, their quest takes on far nobler aims.",
        'image_url': '//image.tmdb.org/t/p/w300//zpaQwR0YViPd83bx1e559QyZ35i.jpg',
        'youtube_url': '//www.youtube.com/embed/Z0cOE2SRo5c?ecver=1'}
    result['comment'] = {
        'comment': '',
        'rating': '',
        'comment_by': '',
        'comment_time': ''}
    result['comments'] = [{
        'comment': '',
        'rating': '',
        'comment_by': '',
        'comment_time': ''}]
    return json.dumps(result)


def get_most_popular_movies():
    result = dict()
    result["movie"] = [
        {
            'movie_id': '',
            'movie_name': '',
            'movie_url': ''
        },
        {
            'movie_id': '',
             'movie_name': '',
             'movie_url': ''
        }]
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


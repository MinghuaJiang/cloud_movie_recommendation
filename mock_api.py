import json


def search():
    result = dict()
    result["query"] = ['Blade Runner', 'Cool Hand Luke', 'Heat', 'Juice', 'Master and Commander: The Far Side of the World', 'Morituri', 'Napoleon Dynamite', 'On The Waterfront', 'Pulp Fiction', 'Rockers', 'Kids', 'Sanjuro', 'The Battle of Algiers', 'Fear and Loathing In Las Vegas', 'The Big Lebowski', 'To Catch a Thief', 'Unstoppable', 'Skyline', 'Harry Potter and the Deathly Hallows - Part 1', 'The Next Three Days', 'Falling Down', 'Fist Full Of Dollars', 'Burlesque', 'Faster', 'Love and Other Drugs', 'Tangled', "The King's Speech", 'Black Swan', "The Warrior's Way", 'The Chronicles of Narnia: The Voyage of the Dawn Treader', 'The Tourist', 'The Tempest', 'The Fighter', 'TRON: Legacy', 'How Do You Know', 'Rabbit Hole', 'Somewhere', 'Little Fockers', 'True Grit', "Gulliver's Travels", 'Blue Valentine', 'Country Strong']
    return json.dumps(result)


def detail(movie_id):
    result = dict()
    result["detail"] = {
        'movie_name': 'Name',
        'movie_average_rating': 4.5,
        'vote_count': 100,
        'genre': ['Action', 'Love'],
        'introduction': "",
        'image_url': '//image.tmdb.org/t/p/w300//zpaQwR0YViPd83bx1e559QyZ35i.jpg',
        'youtube_url': '//www.youtube.com/embed/Z0cOE2SRo5c?ecver=1'}
    result['comments'] = [
        {
        'comment': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare, tellus quis elementum mattis, mauris quam luctus nulla, at consectetur leo dui at massa. In elit mi, suscipit quis fermentum id, convallis mattis tortor. Pellentesque vitae lacus iaculis, malesuada eros in, pharetra sem. Proin sed tellus id metus lobortis molestie at vel turpis. Nulla facilisi.',
        'rating': '9.0',
        'comment_by': 'Donald Trump',
        'comment_time': '2016-04-19'},
        {
        'comment': 'Nulla est odio, eleifend at neque ac, pellentesque consequat metus. Praesent porttitor nunc at sapien fermentum, commodo finibus ante bibendum. Nulla congue, arcu in semper vestibulum, augue lorem blandit tellus, nec suscipit ipsum mauris eget est. Nullam consequat orci nec orci convallis, quis blandit purus blandit. Quisque a vestibulum sapien.',
        'rating': '8.5',
        'comment_by': 'Barrack Obama',
        'comment_time': '2017-03-12'}]
    return json.dumps(result)


def get_most_popular_movies():
    result = dict()
    result["movie"] = [
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        
        {
            'movie_id': '3',
             'movie_name': '3',
             'movie_url': '//image.tmdb.org/t/p/w300//zpaQwR0YViPd83bx1e559QyZ35i.jpg'
        }]
    return json.dumps(result)


def get_paging_most_popular_movies(page):
    result = dict()
    result["movie"] = [
        {
            'movie_id': '3',
            'movie_name': '3',
            'movie_url': '//image.tmdb.org/t/p/w300//zpaQwR0YViPd83bx1e559QyZ35i.jpg'
        },
        {
            'movie_id': '4',
             'movie_name': '4',
             'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/iNpz2DgTsTMPaDRZq2tnbqjL2vF.jpg'
        }]
    return json.dumps(result)


def get_top_rated_movies():
    result = dict()
    result["movie"] = [
        {
            'movie_id': '3',
            'movie_name': '3',
            'movie_url': '//image.tmdb.org/t/p/w300//zpaQwR0YViPd83bx1e559QyZ35i.jpg'
        },
        {
            'movie_id': '4',
             'movie_name': '4',
             'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/iNpz2DgTsTMPaDRZq2tnbqjL2vF.jpg'
        }]
    return json.dumps(result)


def get_paging_top_rated_movies(page):
    result = dict()
    result["movie"] = [
        {
            'movie_id': '3',
            'movie_name': '3',
            'movie_url': '//image.tmdb.org/t/p/w300//zpaQwR0YViPd83bx1e559QyZ35i.jpg'
        },
        {
            'movie_id': '5',
             'movie_name': '5',
             'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/iNpz2DgTsTMPaDRZq2tnbqjL2vF.jpg'
        }]
    return json.dumps(result)


def get_paging_genre_movies(page):
    result = dict()
    result["movie"] = [
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        
        {
            'movie_id': '3',
             'movie_name': '3',
             'movie_url': '//image.tmdb.org/t/p/w300//zpaQwR0YViPd83bx1e559QyZ35i.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        
        {
            'movie_id': '3',
             'movie_name': '3',
             'movie_url': '//image.tmdb.org/t/p/w300//zpaQwR0YViPd83bx1e559QyZ35i.jpg'
        },{
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        {
            'movie_id': '1',
            'movie_name': '1',
            'movie_url': '//image.tmdb.org/t/p/w300_and_h450_bestv2/unPB1iyEeTBcKiLg8W083rlViFH.jpg'
        },
        
        {
            'movie_id': '3',
             'movie_name': '3',
             'movie_url': '//image.tmdb.org/t/p/w300//zpaQwR0YViPd83bx1e559QyZ35i.jpg'
        }]
    return json.dumps(result)


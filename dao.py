from pymongo import MongoClient


class UserDao:
    def __init__(self):
        self.db = MongoClient('184.73.28.43', 27017)['movie-lens']

    def add_new_user(self, username, email, password):
        self.db.user.insert({'username': username, 'email':email, 'password': password, 'isAdmin': False})

    def find_user(self, username):
        return self.db.user.find_one({'username': username})


if __name__ == '__main__':
    userDao = UserDao()
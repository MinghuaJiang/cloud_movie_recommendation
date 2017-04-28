import logging
import json
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, HiddenField
from custom_validators import Username
from wtforms.validators import InputRequired, Email, Length, EqualTo
from dao import MockUserDao
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import mock_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

application = Flask(__name__)
with open('aws_config_secret.json') as cred:
    creds = json.load(cred)
    application.config['SECRET_KEY'] = creds['aws_secret_access_key']
Bootstrap(application)
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'
userDao = MockUserDao()


@login_manager.user_loader
def load_user(username):
    u = userDao.find_user(username)
    if u is None:
        return None
    return User(u['username'])


class User:
    def __init__(self, username):
        self.username = username
        self.email = None

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegistrationForm(FlaskForm):
    email = StringField("email", validators=[InputRequired(), Email(message="invalid email"), Length(max=50)])
    username = StringField('username', validators=[Username(), InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    confirm = PasswordField('retype password',
                            validators=[EqualTo('password', message="password not match"), InputRequired(),
                                        Length(min=8, max=80)])


class ForgotForm(FlaskForm):
    email = StringField("", validators=[InputRequired(), Email(message="invalid email"), Length(max=50)])


class ResetForm(FlaskForm):
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    confirm = PasswordField('retype password',
                            validators=[EqualTo('password', message="password not match"), InputRequired(),
                                        Length(min=8, max=80)])
    token = HiddenField('token')


@application.route("/")
@login_required
def index():
    return render_template('index.html', name=current_user.username)


@application.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = userDao.find_user(form.username.data)
        if user and User.validate_login(user["password"], form.password.data):
            user_obj = User(user['username'])
            login_user(user_obj, remember=form.remember.data)
            return redirect(url_for("index"))

    return render_template('login.html', form=form)


@application.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        userDao.add_new_user(form.username.data, form.email.data, hashed_password)
        user = userDao.find_user(form.username.data)
        user_obj = User(user['username'])
        login_user(user_obj)
        return redirect(url_for("index"))

    return render_template('signup.html', form=form)


@application.route("/forgot", methods=['GET', 'POST'])
def forgot():
    form = ForgotForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        return redirect(url_for('login'))

    return render_template('forgot.html', form=form)


@application.route("/reset", methods=['GET', 'POST'])
def reset():
    form = ResetForm(token=request.args.get("token"))
    if request.method == 'POST' and form.token.data and form.validate_on_submit():
        return redirect(url_for('login'))

    return render_template('reset.html', form=form)


@application.route("/movies/top_rated", methods=['GET'])
def movies_top_rated():
    page = request.args.get('page')
    json = mock_api.get_paging_top_rated_movies()
    return render_template('movie-list.html')


@application.route("/movies/most_popular", methods=['GET'])
def movies_most_popular():
    page = request.args.get('page')
    json = mock_api.get_most_popular_movies()
    return render_template('movie-list.html')


@application.route("/movies/genre/<genre>", methods=['GET'])
def movies_genre(genre):
    page = request.args.get('page')
    json = mock_api.get_paging_genre_movies(page)
    return render_template('movie-list.html')


@application.route("/movie/<int:movie_id>", methods=['GET'])
def movie_detail(movie_id):
    #you can choose to call these api in js as well
    #json = mock_api.detail(movie_id)
    return render_template('movie-detail.html')


@application.route("/search/<query>", methods=['GET'])
def search(query):
    return mock_api.search(query)


@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    application.run()

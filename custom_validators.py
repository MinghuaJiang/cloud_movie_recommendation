from wtforms.validators import ValidationError
from dao import UserDao


class Username(object):
    """
    Validates an username during registration

    :param message:
        Error message to raise in case of a validation error.
    """
    def __init__(self, message=None):
        self.message = message
        self.userDao = UserDao()

    def __call__(self, form, field):
        message = self.message
        if message is None:
            message = field.gettext('Username already exists.')
        if self.userDao.find_user(field.data):
            raise ValidationError(message)


import falcon

from sqlalchemy.orm.exc import NoResultFound
from cerberus import Validator
from cerberus.errors import ValidationError

import logging
from controller.base import BaseResource
from util.authorization import verify_password
from model import User, Base
from util.error.errors import NotValidParameterError, UserNotExistsError, InvalidPassword, AppError, OperationError
from util.validators import validate_login

LOG = logging.get_logger()


class Item(BaseResource):
    """
    /resev/v1/users/login
    """
    @falcon.before(validate_login)
    def on_post(self, req, res):
        data = req.context['data']
        email = data['email']
        password = data['password']
        session = req.context['session']
        try:
            user_db = User.find_by_emails(session, email)
            if verify_password(password, user_db.password.encode('utf-8')):
                self.on_success(res, user_db.to_dict())
            else:
                raise InvalidPassword()
        except NoResultFound:
            raise UserNotExistsError('User email: %s' % email)
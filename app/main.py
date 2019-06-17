"""
Here the main application in order to run gunicorn and
start serving the API REST
"""
import falcon

import log
from wsgiref import simple_server
from middleware import AuthorizationHandler, JSONDecoder, DBSessionManager
from controller import base, user, login
from util.error.errors import AppError
from db import db_session, init_session

LOG = log.get_logger()


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        LOG.info('Starting API Server')

        self.add_route('/', base.BaseResource())
        self.add_route('/umaac/v1/users', user.Collection())
        self.add_route('/umaac/v1/users/{user_id}', user.Item())
        self.add_route('/umaac/v1/users/login', login.Item())
        self.add_error_handler(AppError, AppError.handle)


init_session()
middleware = [AuthorizationHandler(), JSONDecoder(), DBSessionManager(db_session)]
application = App(middleware=middleware)

if __name__ == "__main__":
    httpd = simple_server.make_server('127.0.0.1', 5000, application)
    httpd.serve_forever()
from util.authorization import decrypt_token
from util.error.errors import AuthorizationError
import logging
LOG = logging.get_logger()


class AuthorizationHandler(object):

    def process_request(self, req, res):
        LOG.debug("Authorization: %s", req.auth)
        if req.auth is not None:
            token = decrypt_token(req.auth)
            if token is None:
                raise AuthorizationError('Not valid authorization token: %s' % req.auth)
            else:
                req.context['auth_user'] = token.decode('utf-8')
        else:
            req.context['auth_user'] = None
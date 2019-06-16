import falcon
from util.error.errors import AuthorizationError


def authorization(req, res, resource, params):
    if req.context['auth_user'] is None:
        raise AuthorizationError()
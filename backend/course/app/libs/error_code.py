from app.libs.errors import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class FileSuccess(Success):
    def __init__(self, url):
        super().__init__(msg=url)


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'ServerError'
    error_code = 999


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'resource not found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'


class Duplicate(APIException):
    code = 400
    error_code = 2001
    msg = 'duplicate error'


class Redirect(APIException):
    code = 303
    error_code = 2

    def __init__(self, url):
        super().__init__(msg=url)
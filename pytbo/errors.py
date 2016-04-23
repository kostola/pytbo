# -*- coding: utf-8 -*-

"""
pytbo.errors
~~~~~~~~~~~~

This module implements Pytbo custom errors.

:copyright: (c) 2016 by Alessandro Costa.
:license: Apache2, see LICENSE for more details.

"""

class BotNotFoundError(Exception):
    pass

class BotApiError(Exception):
    pass

class ApiRequestError(BotApiError):
    pass

class ApiResponseError(BotApiError):
    def __init__(self, method, error_code, description):
        super(ApiResponseError, self).__init__("[%s] [%s] %s" % (method, error_code, description))
        self.method = method
        self.error_code = error_code
        self.description = description

class MalformedResponseError(BotApiError):
    pass

# -*- coding: utf-8 -*-

"""
pytbo.bare
~~~~~~~~~~

This module implements a bare Telegram Bot, which is just a wrapper to the Telegram Bots API.

:copyright: (c) 2016 by Alessandro Costa.
:license: Apache2, see LICENSE for more details.

"""

class BareBot(object):
    def __init__(self, token):
        self.token = token

# -*- coding:utf-8 -*-
from functools import wraps
from flask import g
from .errors import forbidden

__author__ = 'liulixiang'


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden(u'权限不够')
            return f(*args, **kwargs)
        return decorated_function
    return decorator

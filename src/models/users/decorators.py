from functools import wraps
from flask import session, request, redirect, url_for

import src


def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        return func(*args, **kwargs)

    return decorated_function


def requires_admin_permissions(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        if session['email'] not in src.config['ADMINS']:
            return redirect(url_for('users.login_user'))
        return func(*args, **kwargs)

    return decorated_function

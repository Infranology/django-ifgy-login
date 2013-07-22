# -*- coding: utf-8 -*-

from django.conf import settings


# Login/Logout
LOGIN_URL = getattr(settings, 'LOGIN_URL', '/login/')
LOGOUT_URL = getattr(settings, 'LOGOUT_URL', '/logout/')
LOGIN_REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', '/')

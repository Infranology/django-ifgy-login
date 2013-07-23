from django.shortcuts import redirect
from django.contrib.auth.views import login, logout


def UserLogin(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/', **kwargs)
    else:
        return login(request, **kwargs)


def UserLogout(request, **kwargs):
    return logout(request, **kwargs)

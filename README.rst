=====
Ifgy Login
=====

ifgy_login is a simple Django app to conduct login and logout.

It uses bootstrap as login page tplt.

Detailed documentation is in the "docs" directory. (not yet!)

Quick start
-----------

1. Add "ifgy_login" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'ifgy_login',
      )

2. Include the ifgy_login URLconf in your project urls.py like this::

      url(r'^', include('ifgy_login.urls')),

Obs.: if you use it with django-cms, must be located prior to cms urls.

3. Start the development server and visit http://127.0.0.1:8000/login/
   you'll need an account in admin(so you'll need the Admin app enabled).

4. Visit http://127.0.0.1:8000/logout/ to logoff your site._

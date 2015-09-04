RJSW
====

A simple site.

Quickstart
----------

If Python 2. ::

    $ virtualenv virtualenv
    $ source virtualenv/bin/activate

If Python 3. ::

    $ pyvenv venv
    $ source venv/bin/activate

Then. ::

    $ pip install Wagtail
    $ pip install django-crispy-forms
    $ cat << END > rjsw/rjsw/settings/__init__.py
    > from .base import *
    > SECRET_KEY = 'ifiwerearichmantralalalalalllalaaalalalalalalalala'
    > DATABASES = {
    >     'default': {
    >         'ENGINE': 'django.db.backends.sqlite3',
    >         'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
    >     }
    > }
    > END
    $ cd rjsw
    $ ./manage syncdb
    $ ./manage runserver











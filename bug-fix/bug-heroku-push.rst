Heroku Push Bug
===============

Setting
-------

1. Cloned repository, trying to push to heroku via::

    git push heroku master

2. Receives the following error::

    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    NameError: name 'install' is not defined

Solution
--------

Heroku is picky about the "distribute" version in requirements.txt

1. Look up current version `here
<https://pypi.python.org/pypi/distribute>`_.

2. Change requirements.txt to that version, for example::

    distribute==0.7.3



Enviromental Monitoring
=======================

Project Layout
--------------

/bug-fix - *Bug fix documentation*
/src - *Source code* 
/images - *Images used in documentation.*
/setup - *Includes documentation for setting up Phidgets and RPi.*
Procfile - *Heroku's way to find the app. Must be at root.*
requirements.txt - *Python dependencies to run the web server.*
routes.py - *Main function with all the routes."*

Running The Webservice (assumes you have completed setup)
---------------------------------------------------------
To run the webservice locally, run the followng commands:

1. This sets up your virtual environment::
    virtualenv venv

2. After that, activate your environment::
    source venv/bin/activate

3. The following only needs to be done once::
    sudo pip install Flask gunicorn

4. Now, run this from the root directory of the project::
    foreman start

That will run the web service at localhost:5000

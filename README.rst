Enviromental Monitoring
=======================

Project Layout
--------------

| /bug-fix - *Bug fix documentation*
| /images - *Images used in documentation.*
| /setup - *Includes documentation for setting up Phidgets and RPi.*
| /src - *Source code* 
|   /aggregation_server
|   /sensor_server
| Procfile - *Heroku's way to find the app. Must be at root.*
| requirements.txt - *Python dependencies to run the web servers.*

Running The Aggregation Webservice
----------------------------------
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

Running The Sensor Webservice
-----------------------------
Please see the /setup folder's README for setting up the sensor server on the Raspberry Pi.

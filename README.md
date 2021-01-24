Full Stack Technical Challenge @UMich
=====================================

Purpose
-------

The purpose of this challenge is to test your full stack abilities within a modern MVC framework and APIs. (We realized that you may not have experience working with one of the web frameworks mentioned below, and we are more interested in your thought process than syntax. If this is the case then please feel free to use pseudo-code, an outline, or diagrams to complete this exercise.)


Challenge
---------

Create a weather web app that allows users to lookup temperatures based on zip code. Please display a minimum of location (name and zip), temperature (Fahrenheit), and day/time (EST); per lookup. Also, the app needs to show all the past records that were searched.


Task Description
----------------

The default page has a input field and a search button. Entering a 5 digit and searching will display the city name, temperature, feels like, humidity and the map if the zip code is valid. If the zip code is not valid, the result will not show any. This is based on what OpenWeather data that is returned. Any input that includes any character will not initiate OpenWeather request. When request is initiated to OpenWeather, all search result will be saved.
In the search history page, all the search history will be displayed. Pagination was used to limit the number of total display in a page, currently set at 5 per page. To change the number of rows in a page, modify `PER_PAGE` value in `logic.py` file.


Dependencies
------------

Python v3.8 was used. Based on the *Purpose* and *Challenge*, this project used Django framework with following libraries to achieve the purpose.

##### python libraries
* Django v3.1.5
* mypy v0.800
* pytz v2020.5
* requests v2.25.1

##### front-end framwork
* Bootstrap v4.6


Installation
------------

### Installation in Windows

* Download and install [Python](https://www.python.org/downloads/). For this guide, Python is assumed to be installed in `C:\Python38`.
* Download the Pip (Python package installer) bootstrap script [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
* In the command prompt, run `C:\Python38\python.exe get-pip.py` to install `pip`.
* In the command prompt, run `C:\Python38\scripts\pip install virtualenv` to install `virtualenv`.

### Installation in Ubuntu

Python 3 is preinstalled in Ubuntu. Virtualenv and pip necessarily aren't, so:

* `sudo apt-get install python-virtualenv python-pip`

### Creating and activating a virtualenv

Go to the project root directory and run:

Windows:

```
c:\location_of_project>c:\Python35\scripts\virtualenv --system-site-packages env
c:\location_of_project>env\Scripts\activate
```

Ubuntu:

```
virtualenv -p /usr/bin/python3 --system-site-packages env
source env/bin/activate
```

Starting the project
--------------------

To start with a fresh SQLite db, remove `db.sqlite3` file on the project's root folder.

After activating the virtualenv,
1. `pip install -r requirements.txt` to install the required libraries.
2. `python manage.py makemigrations` to crate new migrations.
3. `python manage.py migrate --noinput` to apply and unapply migrations.
4. `python manage.py runserver` to run the server.

Now the test should be visible in the browser at [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/).


Testing the project
-------------------

In the project folder with virtualenv activated, run `python manage.py test` to run the test.
The test is not extensive and only tests basic adding data to database.

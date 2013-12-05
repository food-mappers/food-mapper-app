Installation
-------------------------------

Becuase FoodMapper is a [Django](https://www.djangoproject.com/) application, before attempting to install and deploy FoodMapper it would be helpful to be familiarize yourself with [Django](https://www.djangoproject.com/), [python](http://www.python.org/), and [MVC](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) architecture.

We have provided some instructions below to get you started.

1.) Fork the main repo
After the repo is forked and created at 'your-github-username/food-mapper-app', clone your repo

	git clone https://github.com/your-github-username/food-mapper-app.git

or

	git clone git@github.com:your-github-username/food-mapper-app.git

2.) Create new virtual environement
	
	cd food-mapper-app
	virtualenv env
	source env/bin/activate
	pip install -r requirements.txt

3a.) Create the database and users

	createdb food_map_test
	psql -d food_map_test
	CREATE USER foodmapper WITH PASSWORD 'foodmapper';
	GRANT ALL PRIVILEGES ON food_map_test to foodmapper;
	\q

3a.1) You might have trouble with PostGRES when trying to run the app.
To complete the syncdb command, I needed to hack around adding links to the libraries needed by postgres.

First make a directory, then make some symlinks to missing libs.


	mkdir food-mapper-app/env/lib/python2.7/site-packages/lib
	ln -s /Applications/Postgres.app/Contents/MacOS/lib/libssl.1.0.0.dylib food-mapper-app/env/lib/python2.7/site-packages/lib/libssl.1.0.0.dylib
	ln -s /Applications/Postgres.app/Contents/MacOS/lib/libcrypto.1.0.0.dylib food-mapper-app/env/lib/python2.7/site-packages/lib/libcrypto.1.0.0.dylib 

3b.) Run sync db [more on syncdb](https://docs.djangoproject.com/en/dev/ref/django-admin/)

	python manage.py syncdb

seed initial data [more on Django fixtures](https://docs.djangoproject.com/en/dev/howto/initial-data/)

	python manage.py loaddata fixtures/map_data

load a map with a lot of points

	python manage.py loaddata fixtures/lotsofdata


During syncdb create superuser

4.) Start server

	python manage.py runserver

5.) Navigate to root http://127.0.0.1:8000 - Should see the homepage
An application for crowdsourcing food sources in food sheds.

For now we are using the [Fork & Pull Model of development](https://help.github.com/articles/using-pull-requests)

1.) Fork the [main repo](https://github.com/food-mappers/food-mapper-app)

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


	> mkdir food-mapper-app/env/lib/python2.7/site-packages/lib
	> ln -s /Applications/Postgres.app/Contents/MacOS/lib/libssl.1.0.0.dylib food-mapper-app/env/lib/python2.7/site-packages/lib/libssl.1.0.0.dylib
	> ln -s /Applications/Postgres.app/Contents/MacOS/lib/libcrypto.1.0.0.dylib food-mapper-app/env/lib/python2.7/site-packages/lib/libcrypto.1.0.0.dylib 


3b.) Run sync db

	python manage.py syncdb
	#seed initial data
	python manage.py loaddata fixtures/map_data
	#load a map with a lot of points
	python manage.py loaddata fixtures/lotsofdata

During syncdb create superuser

4.) Start server

	python manage.py runserver

5.) Navigate to root [http://127.0.0.1:8000](http://127.0.0.1:8000) - Should see map for now

6.) Signin with user you created - now you can create a community

7.) Navigate to root/communities, create a community

8.) Navigate to root/sources, create a food source.

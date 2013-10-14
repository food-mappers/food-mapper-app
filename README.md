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
	CREATE EXTENSION postgis;
	\q

3b.) Run sync db

	cd src
	python manage.py syncdb
	#seed initial data
	python manage.py loaddata fixtures/map_data

During syncdb create superuser

4.) Start server

	python manage.py runserver

5.) Navigate to root [http://127.0.0.1:8000](http://127.0.0.1:8000) - Should see landing page

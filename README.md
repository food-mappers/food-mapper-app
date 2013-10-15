Justing testing Django REST Framework with our data model.  Taking a lot from the Django REST Framework tutorial [here](http://django-rest-framework.org/tutorial/quickstart.html)

Not using POSTGRESQL but SQLITE3 for now

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

3.) Run sync db

	cd src
	python manage.py syncdb
	#seed initial data
	python manage.py loaddata fixtures/community_data

During syncdb create superuser

4.) Start server

	python manage.py runserver

5.) Navigate to root [http://127.0.0.1:8000](http://127.0.0.1:8000) - Should see map for now

6.) Signin with user you created - now you can create a community

7.) Navigate to root/communities, create a community

8.) Navigate to root/sources, create a food source.


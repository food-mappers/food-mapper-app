Justing testing Django REST Framework with our data model.  Taking a lot from the Django REST Framework tutorial [here](http://django-rest-framework.org/tutorial/quickstart.html)

Not using POSTGRESQL but SQLITE3 for now

1.) Clone repo

	git clone https://github.com/food-mappers/rest-framework-dev.git

or

	git clone git@github.com:food-mappers/rest-framework-dev.git

2.) Create new virtual environement

	cd rest-framework-dev
	virtualenv env
	source env/bin/activate
	pip install -r requirements.txt

3.) Run sync db

	cd src
	python src/manage.py syncdb

During syncdb create superuser

4.) Start server

	python src/manage.py runserver

5.) Navigate to root [http://127.0.0.1:8000](http://127.0.0.1:8000)

6.) Signin with user you created - now you can create a community

7.) Navigate to root/communities, create a community

8.) Navigate to root/sources, create a food source


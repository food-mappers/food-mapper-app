Architecture of techniques
----------

* [Django](https://github.com/django/djangoproject)
* [Twitter Bootstrap](https://github.com/twbs/bootstrap) 		
* [LeafletJS](https://github.com/Leaflet/Leaflet)  
* [PostgreSQL](http://www.postgresql.org/)



Our project include a service based application on different platform, including a Django web side location based application which backed back PostGRES database which is suitable for geo-data. 

Architecture of source code
----------


**api** - A Django app that provides models, views, serializers, and urls for the API that is used in FoodMapper.  This code heavily utilizes the [Django REST Framework project](http://django-rest-framework.org/).  To begin working on this part of the application, please check out the Django REST Framework [tutorial](http://django-rest-framework.org/tutorial/quickstart) to understand how this works.
 
**fixtures** - A folder that contains seed data useful in in populating the database for development purposes.  To [seed data](https://docs.djangoproject.com/en/dev/howto/initial-data/) run the following command from the Django project:
	
	python manage.py loadfixtures fixtures/map_data.json

or

	python manage.py loadfixtures fixtures/lotsofdata.json

For more on fixtures please see the [Django documentation](https://docs.djangoproject.com/en/dev/howto/initial-data/.
 
**foodmapperapp** - Folder created that houses the Django project.  This folder contains settings.py which configures the Django application and loads all submodules,  urls.py loads the url patterns for the api, frontend, and admin apps.

**frontend** - Another Django app for managing the front end code and interactions with the api. This app also contains the static components like the HTML 

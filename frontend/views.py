from django.shortcuts import render
from django.template.response import TemplateResponse
from api.models import Map
from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
	return render(request, 'root.html')

def page_not_found(request):
	return render(request, '404.html')

def login(request):
	return TemplateResponse(request, 'login.html', {'request': request})

def maps(request):
	return render(request, 'maps.html', {'maps' : Map.objects.all()})

def map(request, slug):
	current_map = Map.objects.filter(namespace=slug)
	if current_map:
		return render(request, 'map.html', {'map' : serializers.serialize("json", current_map), 'title' : current_map[0].name})
	else:
		raise Http404

@login_required
def user(request, username):
	if (request.user.username == username):
		return render(request, 'user.html')
	else:
		raise Http404

@login_required
def usermaps(request, username):
	if (request.user.username == username):
		return render(request, 'adminMyMaps.html', {'maps': Map.objects.filter(owner=request.user.pk)})
	else:
		raise Http404
from django.shortcuts import render
from django.template.response import TemplateResponse
from api.models import Map, Source
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
	sources = Source.objects.filter(map=current_map[0].id, status=True)
	bbox = getBbox(sources)
	if current_map:
		return render(request, 'map.html', {'map' : serializers.serialize("json", current_map), 'title' : current_map[0].name, 'bbox' : bbox})
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

def getBbox(sources):
	bbox = [[-180,-180],[180,180]]
	if len(sources) == 0:
		return [[33.9444992073, -83.9595794677],[33.5894553355, -84.7924804]]
	for source in sources:
		if source.latitude > bbox[0][0]:
			bbox[0][0] = float(source.latitude)
		if source.longitude > bbox[0][1]:
			bbox[0][1] = float(source.longitude)
		if source.latitude < bbox[1][0]:
			bbox[1][0] = float(source.latitude)
		if source.longitude < bbox[1][1]:
			bbox[1][1] = float(source.longitude)
	return bbox
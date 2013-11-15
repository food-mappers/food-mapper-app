from django.shortcuts import render
from django.template.response import TemplateResponse
from api.models import Map, Source
from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
	return render(request, 'root.html')

def page_not_found(request):
	return render(request, '404.html')

def login(request):
	return TemplateResponse(request, 'login.html', {'request': request})

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def maps(request):
	return render(request, 'maps.html', {'maps' : Map.objects.all()})

def addmap(request):
	if request.method == 'POST':
		if request.user.is_authenticated():
			map = Map(name=request.POST.get('name'), owner=request.user, description=request.POST.get('description'))
			map.save()
			return HttpResponseRedirect('/map/' + map.namespace)
		else:
			return HttpResponseRedirect('/login/?next=/maps/add')
	return render(request, 'addMap.html')

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

@login_required
def usersources(request, username):
	if (request.user.username == username):
		return render(request, 'adminMySources.html', {'sources': Source.objects.filter(owner=request.user.pk)})
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

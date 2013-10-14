from django.shortcuts import render
from django.template.response import TemplateResponse
from api.models import Map
from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponseNotFound



def index(request):
	return render(request, 'root.html')

def login(request):
	return TemplateResponse(request, 'login.html', {'request': request})

def maps(request):
	return render(request, 'maps.html', {'maps' : Map.objects.all()})

def map(request, slug):
	current_map = Map.objects.filter(namespace=slug)
	if current_map:
		return render(request, 'map.html', {'map' : serializers.serialize("json", current_map), 'title' : current_map[0].name})
	else:
		return HttpResponseNotFound('<h1>Could not find that map</h1>')
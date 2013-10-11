from django.shortcuts import render
from api.models import Map
from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponseNotFound



def index(request):
	current_map = Map.objects.filter(namespace='public')
	return render(request, 'index.html', {'map': serializers.serialize("json", current_map)})

def map(request, slug):
	current_map = Map.objects.filter(namespace=slug)
	if current_map:
		return render(request, 'index.html', {'map' : serializers.serialize("json", current_map)})
	else:
		return HttpResponseNotFound('<h1>Could not find that map</h1>')
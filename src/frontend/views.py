from django.shortcuts import render
from api.models import Community
from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponseNotFound



def index(request):
	current_community = Community.objects.filter(namespace='public')
	return render(request, 'index.html', {'community': serializers.serialize("json", current_community)})

def community_map(request, slug):
	current_community = Community.objects.filter(namespace=slug)
	if current_community:
		return render(request, 'index.html', {'community' : serializers.serialize("json", current_community)})
	else:
		return HttpResponseNotFound('<h1>Could not find that community</h1>')
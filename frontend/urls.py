from django.conf.urls import patterns, url, include
from frontend import views
from django.views.generic import TemplateView


print views

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index'),
    url(r'^login', 'frontend.views.login'),
    url(r'^maps', 'frontend.views.maps'),
    url(r'^map/(?P<slug>[-\w]+)','frontend.views.map')
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
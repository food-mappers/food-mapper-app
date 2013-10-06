from django.conf.urls import patterns, url, include
from frontend import views
from django.views.generic import TemplateView


print views

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index'),
    url(r'^community/(?P<slug>[-\w]+)','frontend.views.community_map')
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
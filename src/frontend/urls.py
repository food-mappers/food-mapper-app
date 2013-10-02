from django.conf.urls import patterns, url, include
from frontend import views
from django.views.generic import TemplateView


print views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
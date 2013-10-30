from api.models import Source, Map, Comment
from api.serializers import SourceSerializer, MapSerializer, CommentSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import link
import django_filters


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'sources': reverse('source-list', request=request, format=format)
    })

class MapViewSet(viewsets.ModelViewSet):
	queryset = Map.objects.filter(status=True)
	serializer_class = MapSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	def pre_save(self, obj):
		obj.owner = self.request.user

class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = ['map']

class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['source', 'owner']

class SourceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Source.objects.filter(status=True)
    serializer_class = SourceSerializer
    filter_class = SourceFilter

    def pre_save(self, obj):
        
        if (self.request.user.is_authenticated()):
            obj.owner = self.request.user

    def post_save(self, source, *args, **kwargs):
        if type(source.tags) is list:
            saved_source = Source.objects.get(pk=source.pk)
            for tag in source.tags:
                saved_source.tags.add(tag)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Automatically provides 'list' and 'detail' actions
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_class = CommentFilter
    
    def pre_save(self, obj):
        if (self.request.user.is_authenticated()):
            obj.owner = self.request.user
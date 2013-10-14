from api.models import Source, Map
from api.serializers import SourceSerializer, MapSerializer
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


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'sources': reverse('source-list', request=request, format=format)
    })

class MapViewSet(viewsets.ModelViewSet):
	queryset = Map.objects.all()
	serializer_class = MapSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	def pre_save(self, obj):
		obj.owner = self.request.user

class SourceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)

    @link(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def pre_save(self, obj):
        if (self.request.user.is_authenticated()):
            obj.owner = self.request.user

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Automatically provides 'list' and 'detail' actions
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
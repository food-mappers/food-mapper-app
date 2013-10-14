from django.forms import widgets
from rest_framework import serializers
from api.models import Source, Map
from django.contrib.auth.models import User

class SourceSerializer(serializers.ModelSerializer):
    # user = serializers.Field(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    # communities = serializers.HyperlinkedRelatedField(view_name='community-detail', lookup_field='name', required=False, read_only=True)
    # community = serializers
    user = serializers.Field(source='owner')

    class Meta:
        model = Source
        fields = ('name', 'description', 'latitude', 'longitude', 'map', 'user')
        

class MapSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.Field(source='owner.username')
    sources = SourceSerializer(many=True, read_only=True)
    class Meta:
        model = Map
        fields = ('name', 'namespace', 'id', 'sources')
        # read_only_fields = ('namespace')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # communities = serializers.HyperlinkedRelatedField(many=True, view_name='community-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'map')
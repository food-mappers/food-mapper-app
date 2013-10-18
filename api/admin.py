from django.contrib import admin
from api.models import Source, Map

class SourceAdmin(admin.ModelAdmin):
	pass

class MapAdmin(admin.ModelAdmin):
	pass

admin.site.register(Source, SourceAdmin)
admin.site.register(Map, MapAdmin)
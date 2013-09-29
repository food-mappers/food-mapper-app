from django.contrib import admin
from api.models import Source, Community

class SourceAdmin(admin.ModelAdmin):
	pass

class CommunityAdmin(admin.ModelAdmin):
	pass

admin.site.register(Source, SourceAdmin)
admin.site.register(Community, CommunityAdmin)
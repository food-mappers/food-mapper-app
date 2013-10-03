# from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField

from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.conf import settings
from django.core.files.storage import get_storage_class
from django.core.urlresolvers import reverse

# Create your models here.

class TimeStampedModel (models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class Community(TimeStampedModel):
	name = models.CharField(max_length=50)
	namespace = AutoSlugField(populate_from='name', unique=True)
	owner = models.ForeignKey('auth.User', related_name='community')

	def save(self, *args, **kwargs):
		# print self
		# s.community = self.community
		# s.save()
		self.namespace = slugify(self.name)
		super(Community, self).save(*args, **kwargs)

# class Place (models.Model):
# 
#     location = models.PointField()
#     community = models.ManyToManyField(Community)
#     objects = models.GeoManager()
#     
#     def save(self, *args, **kwargs):
# 		print self.name
# 		# print Community.objects.get(name="Public").object_id
# 		# self.community = 1#Community.objects.get(name="Public")
# 		super(Source, self).save(*args, **kwargs)
# 		# self.community.add(Community.objects.get(name="Public"))
# 		# self.save()
# 
# #     class Meta:
# #         db_table = 'food_map_place'
# #         managed = False

class Source(TimeStampedModel):
	#created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=150)
	description = models.CharField(max_length=300)
	#latitude = models.DecimalField(max_digits=30, decimal_places=27)
	#longitude = models.DecimalField(max_digits=30, decimal_places=27)
	# user = models.ForeignKey('auth.User', related_name='foodsource')
	community = models.ForeignKey(Community, related_name='sources')
	location = models.PointField()
	
	def save(self, *args, **kwargs):
		print self.name
		# print Community.objects.get(name="Public").object_id
		# self.community = 1#Community.objects.get(name="Public")
		super(Source, self).save(*args, **kwargs)
		# self.community.add(Community.objects.get(name="Public"))
		# self.save()
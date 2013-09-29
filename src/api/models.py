from django.db import models

# Create your models here.

class Community(models.Model):
	name = models.CharField(max_length=50)
	namespace = models.CharField(max_length=60)
	owner = models.ForeignKey('auth.User', related_name='community')

	def save(self, *args, **kwargs):
		# print self
		# s.community = self.community
		# s.save()
		super(Community, self).save(*args, **kwargs)



class Source(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=150)
	description = models.CharField(max_length=300)
	latitude = models.DecimalField(max_digits=15, decimal_places=12)
	longitude = models.DecimalField(max_digits=15, decimal_places=12)
	# user = models.ForeignKey('auth.User', related_name='foodsource')
	community = models.ForeignKey(Community, related_name='sources')

	def save(self, *args, **kwargs):
		print self.name
		# print Community.objects.get(name="Public").object_id
		# self.community = 1#Community.objects.get(name="Public")
		super(Source, self).save(*args, **kwargs)
		# self.community.add(Community.objects.get(name="Public"))
		# self.save()
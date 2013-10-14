from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField

# Create your models here.

class Map(models.Model):
    name = models.CharField(max_length=50)
    namespace = AutoSlugField(populate_from='name', unique=True)
    description = models.CharField(max_length=350, null=True)
    owner = models.ForeignKey('auth.User', related_name='map')

    def save(self, *args, **kwargs):
        # print self
        # s.map = self.map
        # s.save()
        self.namespace = slugify(self.name)
        super(Map, self).save(*args, **kwargs)
    class Meta :
        db_table = "map"    



class Source(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    latitude = models.DecimalField(max_digits=30, decimal_places=27)
    longitude = models.DecimalField(max_digits=30, decimal_places=27)
    owner = models.ForeignKey('auth.User', related_name='source', null=True)
    map = models.ForeignKey(Map, related_name='sources')

    def save(self, *args, **kwargs):
        # print self.name
        print self.owner
        # print Map.objects.get(name="Public").object_id
        # self.map = 1#Map.objects.get(name="Public")
        super(Source, self).save(*args, **kwargs)
        # self.map.add(Map.objects.get(name="Public"))
        # self.save()
    class Meta :
        db_table = "source"        
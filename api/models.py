# from django.db import models
from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

class Map(models.Model):
    name = models.CharField(max_length=50)
    namespace = AutoSlugField(populate_from='name', unique=True)
    description = models.CharField(max_length=350, null=True)
    owner = models.ForeignKey('auth.User', related_name='map')
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.namespace = slugify(self.name)
        super(Map, self).save(*args, **kwargs)
    class Meta :
        db_table = "map"

    def __unicode__(self):
        return str(self.name) + ": " + str(self.description)

class Source(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    latitude = models.DecimalField(max_digits=30, decimal_places=27)
    longitude = models.DecimalField(max_digits=30, decimal_places=27)
    owner = models.ForeignKey('auth.User', related_name='source', null=True)
    map = models.ForeignKey(Map, related_name='sources')
    status = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Source, self).save(*args, **kwargs)
        
    class Meta :
        db_table = "source"

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='comment', null=True)
    content = models.CharField(max_length=400, null=True)
    source = models.ForeignKey(Source, related_name='comments')

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
    class Meta:
        db_table = "comment"      

class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', related_name='profile', unique=True)
    orgname = models.CharField(max_length=150)

    def __unicode__(self):
        return "user profile for " + self.user.name

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        db_table = 'userprofile'

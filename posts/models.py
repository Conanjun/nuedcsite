from django.db import models
from tinymce.models import HTMLField
from django.contrib import admin

# Create your models here.
class NewsPost(models.Model):
	title = models.CharField(max_length=50)
	content = HTMLField()
	uptime = models.DateTimeField(auto_now=True)
	rating = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title

class NotifyPost(models.Model):
	title = models.CharField(max_length=50)
	content = HTMLField()
	uptime = models.DateTimeField(auto_now=True)
	rating = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title	

class NewsPostAdmin(admin.ModelAdmin):
	list_display = ["title","uptime"]

class NotifyPostAdmin(admin.ModelAdmin):
	list_display = ["title","uptime"]

admin.site.register(NewsPost,NewsPostAdmin)
admin.site.register(NotifyPost,NotifyPostAdmin)
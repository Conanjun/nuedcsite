from django.db import models
from django.contrib import admin
from NuedcSite.settings import  MEDIA_ROOT

# Create your models here.
class UpFile(models.Model):
    title = models.CharField(max_length=50)
    descript = models.CharField(max_length=150)
    upfile = models.FileField(upload_to="upfiles/")
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.upfile.name


class FileAdmin(admin.ModelAdmin):
    list_display = ["title","descript","created"]

admin.site.register(UpFile,FileAdmin)
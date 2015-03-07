# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
from string import join
import os
from PIL import Image as PImage
from NuedcSite.settings import  MEDIA_ROOT

    
class Image(models.Model):
    image = models.FileField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    #album = models.ForeignKey(Album)

    class Meta: 
        ordering = ['-id']
        verbose_name = u"照片"
        verbose_name_plural = "照片列表"

    def __unicode__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size
        super(Image, self).save(*args, ** kwargs)

    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))
    thumbnail.allow_tags = True

    
class Album(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    image = models.ManyToManyField(Image, blank = True, null = True)
    rating = models.IntegerField(default=0)

    class Meta: 
        ordering = ['-rating']
        verbose_name = u"相册"
        verbose_name_plural = "相册列表"
        
    def cover(self):
        cover = self.image.all()
        return cover[0].image.name

    def date(self):
        cover = self.image.all()
        return cover[0].created

    def __unicode__(self):
        return self.title

    def images(self):
        lst = [x.image.name for x in self.image.all()]
        lst = ["""<img border="0" src="/media/%s"  title="%s"  height="40" />""" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')
    images.allow_tags = True


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title","images"]

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    # search_fields = ["title"]
    list_display = ["__unicode__","image","rating", "size","thumbnail", "created"]
    #list_filter = ["tags", "albums"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)
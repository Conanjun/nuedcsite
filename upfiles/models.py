# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
from NuedcSite.settings import  MEDIA_ROOT

# Create your models here.
class UpFile(models.Model):
    title = models.CharField(max_length=50, verbose_name = u"标题")
    descript = models.CharField(max_length=150, verbose_name = u"文件描述")
    upfile = models.FileField(upload_to="upfiles/", verbose_name = u"文件")
    created = models.DateTimeField(auto_now_add=True, verbose_name = u"上传时间")
    rating = models.IntegerField(default=0, verbose_name = u"点击量")

    def __unicode__(self):
        return self.upfile.name

    class Meta: 
        verbose_name = u"上传文件"
        verbose_name_plural = "上传文件列表"


class FileAdmin(admin.ModelAdmin):
    list_display = ["title","descript","created"]

admin.site.register(UpFile,FileAdmin)
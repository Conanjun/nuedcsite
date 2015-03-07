# -*- coding:utf-8 -*-
from django.db import models
from tinymce.models import HTMLField
from django.contrib import admin


# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=50, verbose_name = u"标题")
    content = HTMLField(verbose_name = u"正文")
    uptime = models.DateTimeField(auto_now=True, verbose_name = u"发布日期")
    rating = models.IntegerField(default=0, verbose_name = u"点击量")
    author = models.CharField(max_length=50, verbose_name = u"作者")

    def __unicode__(self):
        return self.title

    class Meta: 
        verbose_name = u"新闻"
        verbose_name_plural = "新闻列表"


class NotifyPost(models.Model):
    title = models.CharField(max_length=50, verbose_name = u"标题")
    content = HTMLField(verbose_name = u"正文")
    uptime = models.DateTimeField(auto_now=True, verbose_name = u"发布日期")
    rating = models.IntegerField(default=0, verbose_name = u"点击量")
    author = models.CharField(max_length=50, verbose_name = u"作者")

    def __unicode__(self):
        return self.title

    class Meta: 
        verbose_name = u"通知"
        verbose_name_plural = "通知列表"


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ["title","uptime"]


class NotifyPostAdmin(admin.ModelAdmin):
    list_display = ["title","uptime"]

admin.site.register(NewsPost,NewsPostAdmin)
admin.site.register(NotifyPost,NotifyPostAdmin)
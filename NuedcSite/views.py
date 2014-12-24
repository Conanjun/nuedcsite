from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from upfiles.models import *
from posts.models import *
import os


def home(request):
    news_list = NewsPost.objects.all()
    max_rating_news = NewsPost.objects.order_by("-rating")[0:5]
    notify_list=NotifyPost.objects.all()
    max_rating_notify = NotifyPost.objects.order_by("-rating")[0:5]

    return render_to_response('home.html',{"nav":"home","news_list":news_list,"max_rating_news":max_rating_news,"notify_list":notify_list,"max_rating_notify":max_rating_notify})

# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext  
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db import connection

from posts.models import *

COUNT_PER_PAGE = 2
range_len = 3

# Create your views here.
def news_index(request):
    news_list = NewsPost.objects.all()
    side_list = NewsPost.objects.order_by("-uptime")[0:12]
    paginator = Paginator(news_list, COUNT_PER_PAGE)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        this_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        if page == 0:
            this_page = paginator.page(1)
        else:
            this_page = paginator.page(paginator.num_pages)
    if page > range_len:
        page_range = paginator.page_range[page-range_len:page]
    else:
        page_range = paginator.page_range[0:range_len]
    return render_to_response('news_list.html',{"nav":"news","news_list": this_page,"length": page_range,
                               "side_list": side_list},)


def show_article(request):
    Id = request.GET.get('id')
    ID=int(Id)
    item = NewsPost.objects.get(id=Id)
    max = NewsPost.objects.count()
    side_list = NewsPost.objects.order_by("-uptime")[0:12]
    num = ID%COUNT_PER_PAGE
    page = ID/COUNT_PER_PAGE
    if num!=0:
        page +=1
    id1=ID-1
    id2=ID+1
    if id1<1:
        id1=1
    if id2>max:
        id2=max
    item.rating +=1
    item.save
    return render_to_response('news_content.html',{"nav":"news", "title":item.title,"id1":id1,"id2":id2,"content":item.content,
                                                   "uptime":item.uptime,"author":item.author, "rating":item.rating,
                                                   'page':page,"side_list": side_list})

def notifies_index(request):
    notify_list = NotifyPost.objects.all()
    side_list = NewsPost.objects.order_by("-uptime")[0:12]
    paginator = Paginator(notify_list, COUNT_PER_PAGE)
    pages_count = paginator.num_pages
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        this_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        if page == 0:
            this_page = paginator.page(1)
        else:
            this_page = paginator.page(paginator.num_pages)
    if page > range_len:
        page_range = paginator.page_range[page-range_len:page]
    else:
        page_range = paginator.page_range[0:range_len]
    return render_to_response('notify_list.html',{"nav":"notify","notify_list":this_page,"length":page_range,
                                                  "side_list": side_list})

def show_notify(request):
    return render_to_response('news_content.html',{"nav":"news"})
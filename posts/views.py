# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext  
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from posts.models import *

COUNT_PER_PAGE = 5
after_range_num = 5
before_range_num = 4

# Create your views here.
def news_index(request):
    news_list = NewsPost.objects.all()
    paginator = Paginator(news_list, COUNT_PER_PAGE)
    pages_count = paginator.num_pages
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        this_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        this_page = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]
    return render_to_response('news_list.html',{"nav":"news","news_list":news_list,"length":page_range})

def show_article(request):
    return render_to_response('news_content.html',{"nav":"news"})

def notifies_index(request):
    news_list = NewsPost.objects.all()
    paginator = Paginator(news_list, COUNT_PER_PAGE)
    pages_count = paginator.num_pages
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        this_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        this_page = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]
    return render_to_response('news_list.html',{"nav":"news","news_list":news_list,"length":page_range})

def show_notify(request):
    return render_to_response('news_content.html',{"nav":"news"})
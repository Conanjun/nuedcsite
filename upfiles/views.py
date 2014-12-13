# Create your views here.
from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from upfiles.models import *
import os

COUNT_PER_PAGE = 4
range_len = 5

def index(request):
    file_list = UpFile.objects.all()
    paginator = Paginator(file_list, COUNT_PER_PAGE)
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
        page_range = paginator.page_range[page-1:page+range_len-1]
    else:
        page_range = paginator.page_range[0:range_len]
    return render_to_response('upfile_list.html',{"nav":"upfiles","this_page": this_page,"length":page_range})

def count(request):
    a=1
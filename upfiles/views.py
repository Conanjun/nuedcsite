# Create your views here.
from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from upfiles.models import *
import os

COUNT_PER_PAGE = 5
after_range_num = 5
befor_range_num = 4

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
        this_page = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]     
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    return render_to_response('upfile_list.html',{"nav":"upfiles","this_page": this_page,"length":page_range})
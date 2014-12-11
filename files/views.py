# Create your views here.
from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from files.models import *
import os

FILE_COUNT_PER_PAGE	= 5

def index(request):
	file_list = UpFile.objects.all()
	paginator = Paginator(file_list, FILE_COUNT_PER_PAGE)
	pages_count = paginator.num_pages
	length = [i for i in range(1,pages_count+1)]
	try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        this_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        this_page = paginator.page(paginator.num_pages)
    return render_to_response('upfile_list.html',{"this_page": this_page,"length": length})
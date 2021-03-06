# Create your views here.
# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext  
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from album.models import *

COUNT_PER_PAGE = 5
after_range_num = 5
before_range_num = 4

def album_index(request):
    album_list = Album.objects.all()
    paginator = Paginator(album_list, COUNT_PER_PAGE)
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
    return render_to_response('album_list.html',{"nav":"album","album_list":album_list,"length":page_range})

def album_content(request,album_id):
    this_album = Album.objects.get(id=album_id)
    this_album.rating += 1
    this_album.save()
    return render_to_response('album_content.html',{"album":this_album,})

def image_content(request,album_id,image_id):
    this_image = Image.objects.get(id=image_id)
    this_image.rating += 1
    this_image.save()
    return render_to_response('image_content.html',{"image":this_image,"album":album_id,})

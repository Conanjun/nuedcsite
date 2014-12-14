# Create your views here.
from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from upfiles.models import *
import os

COUNT_PER_PAGE = 1
range_len = 3
@csrf_protect
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
        page_range = paginator.page_range[page-range_len:page]
    else:
        page_range = paginator.page_range[0:range_len]
    return render_to_response('upfile_list.html',{"nav":"upfiles","this_page": this_page,"length":page_range},context_instance=RequestContext(request))

def download(request):
    if request.method == 'POST' and request.POST.has_key('btn'):
        Id = request.POST.__getitem__('btn')
        item = UpFile.objects.get(id=Id)
        item.rating += 1
        item.save()
        src = request.GET.get('add').encode('utf-8')
        tem=src.split('/')
        filename=tem[3]
        wrapper = FileWrapper(file(src))
        response = HttpResponse(wrapper, content_type='text/plain')
        response['Content-Length'] = os.path.getsize(src)
        response['Content-Encoding'] = 'utf-8'
        response['Content-Disposition'] = 'attachment;filename=%s' % filename
        return response
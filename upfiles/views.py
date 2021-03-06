# Create your views here.
from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from upfiles.models import *
import os

COUNT_PER_PAGE = 2
range_len = 3
@csrf_protect
def index(request):
    file_list = UpFile.objects.all()
    side_list = UpFile.objects.order_by("-created")[0:12]
    paginator = Paginator(file_list, COUNT_PER_PAGE)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        this_page = paginator.page(page)
        if type(this_page.next_page_number) != type(1):
            this_page.next_page_number = this_page.number
        if type(this_page.previous_page_number) != type(1):
           this_page.previous_page_number = this_page.number 
    except (EmptyPage, InvalidPage):
        this_page = paginator.page(paginator.num_pages)
    if page > range_len:
        page_range = paginator.page_range[page-range_len:page]
    else:
        page_range = paginator.page_range[0:range_len]
    return render_to_response('upfile_list.html',{"nav":"upfiles","this_page": this_page,"length": page_range,
                               "side_list": side_list}, context_instance=RequestContext(request))
@csrf_protect
def show_content(request):
    Id = request.GET.get('id')
    ID=int(Id)
    item = UpFile.objects.get(id=Id)
    max = UpFile.objects.count()
    side_list = UpFile.objects.order_by("-created")[0:12]
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
    return render_to_response('upfile_content.html',{"nav":"upfiles",'src':item.upfile.name,"id":ID,"id1":id1,"id2":id2,"title":item.title,"descript":item.descript,
                                                   "created":item.created,"rating":item.rating,'page':page,"side_list": side_list}, context_instance=RequestContext(request))

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
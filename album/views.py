# Create your views here.
# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from album.models import *
from PIL import Image
import datetime
import os

def show_contents(request,album_id):
    n_album = Album.objects.get(id=album_id)
    n_album.views_amount += 1
    n_album.save()
    i_photo = Image.objects.filter(belong=album_id)
    return render_to_response('show_albums.html',{'photo_list': i_photo,'intro': n_album.intro})

def show_albums(request):
    album_list =  Album.objects.all()
    return render_to_response('show_albums.html',{'album_list': album_list})

def upload_intro(request):
    if request.method == 'POST':
        if request.POST['url']:
            photo = Photo.objects.get(full_url=request.POST['url'])
            photo.intro = request.POST['photo_intro']
            photo.save()
    album_list =  Album.objects.all()
    return render_to_response('upload.html',{'album_list': album_list,})

def upload(request):
    album_list =  Album.objects.all()
    errors = []
    photo_url = ''
    if request.method == 'POST':
        errors = ifError(request,album_list)
        if not errors:
            if request.POST['album_name']=='new':
                new_album(request)
                album_list =  Album.objects.all()
            try:
                img = Image.open(request.FILES['picfile'])
                new_photo = newPhoto(request.POST['title'])
                save_img(img,new_photo.micro_url[1:],new_photo.full_url[1:])
                photo_url = new_photo.full_url
            except Exception,e:
                errors.append(e)
    return render_to_response('upload.html',{'errors': errors,'album_list': album_list,'url': photo_url,})

def ifError(request,album_list):
    errors = []
    if "Choose a album" == request.POST['album_name']:
        errors.append('请选择或创建一个相册')
    if request.POST['album_name']=='new':
        if not request.POST['title']:
            errors.append('请输入相册名')
        for i in album_list:
            if i.title == request.POST['title']:
                errors.append('同名相册已存在')
    return errors

def new_album(request):
    new_album = Album()
    new_album.title = request.POST['title']
    if request.POST['album_intro'] and request.POST['album_name']=='new':
        new_album.intro = request.POST['album_intro']
    new_album.up_date = datetime.datetime.now()
    new_album.amount = 0
    new_album.views_amount = 0
    new_album.author = "Admin"
    new_album.save()

def newPhoto(title):
    n_album = Album.objects.get(title=title)
    n_album.cover_url = "/static/images/micro/%sn%s.jpg"%(n_album.id,str(n_album.amount))
    n_album.up_date = datetime.datetime.now()
    n_album.amount+=1
    n_album.save()

    new_photo = Photo()
    new_photo.micro_url = n_album.cover_url
    new_photo.full_url = "/static/images/full/%sn%s.jpg"%(n_album.id,str(n_album.amount-1))
    #if request.POST['photo_intro']:
        #new_photo.intro = request.POST['photo_intro']
    new_photo.click_num = 0
    new_photo.belong = n_album.id
    new_photo.up_date = datetime.datetime.now()
    new_photo.save()
    return new_photo

def save_img(img,micro_url,full_url):
    SITE_ROOT=os.path.join(os.path.abspath(os.path.dirname(__file__)),'..')
    img.thumbnail((4096,4096),Image.ANTIALIAS)
    img.save(os.path.join(SITE_ROOT,full_url),'jpeg')

    n = img.size
    if n[0]>n[1]:
        n1 = int((n[0]-n[1])/2)
        img = img.crop((n1,0,n1+n[1],n[1]))
    elif n[1]>n[0]:
        n1 = int((n[1]-n[0])/2)
        img = img.crop((0,n1,n[0],n1+n[0]))

    img.thumbnail((128,128),Image.ANTIALIAS)
    img.save(os.path.join(SITE_ROOT,micro_url),'jpeg')

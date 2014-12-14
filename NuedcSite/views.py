from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from upfiles.models import *
import os


def home(request):

    return render_to_response('home.html')
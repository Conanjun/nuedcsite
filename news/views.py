# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext  
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render_to_response('news_list.html')


def show_article(request):
	return render_to_response('news_content.html')
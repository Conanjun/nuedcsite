from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'upfiles.views.index', name='files_index'),
    url(r'^download$', 'upfiles.views.download', name='download')
)

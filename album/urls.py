from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'album.views.album_index', name='album_index'),
    url(r'^(\d*)/$', 'album.views.album_content', name='album_content'),
    url(r'^images/(\d*)n(\d*)/$', 'album.views.image_content', name='image_content'),
)

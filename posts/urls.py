from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^news/', 'posts.views.news_index', name='news_index'),
    url(r'^news_article/','posts.views.show_article',name='show_article'),
)

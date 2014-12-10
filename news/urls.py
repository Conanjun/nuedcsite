from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'news.views.index', name='news_index'),
    url(r'^article/','news.views.show_article',name='show_article'),
)

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^news/', 'posts.views.news_index', name='news_index'),
    url(r'^news_item/','posts.views.show_article',name='show_article'),
    url(r'notify/','posts.views.notifies_index',name='notifies_index'),
    url(r'notify_item/','posts.views.show_notify',name='show_notify'),
)

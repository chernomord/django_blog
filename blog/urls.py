from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<post_name>.+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<post_name>.+)/$', views.post_detail, name='post_detail'),
]

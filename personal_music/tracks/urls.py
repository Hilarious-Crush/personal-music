from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^genre/list$', views.genre_list, name='genre_list'),
    url(r'^genre/(?P<id>\d+)/$', views.genre_page, name='genre_page'),
    url(r'^artist/list/$', views.artist_list, name='artist_list'),
    url(r'^artist/(?P<id>\d+)/$', views.artist_page, name='artist_page'),
]
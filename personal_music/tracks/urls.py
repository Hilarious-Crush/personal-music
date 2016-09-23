from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^genre$', views.genre, name='genre'),
    url(r'^artist/list/$', views.artist_list, name='artist_list'),
    url(r'^artist/(?P<id>\d+)/$', views.artist_page, name='artist_page'),

]
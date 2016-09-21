from django.conf.urls import url
from . import views, urls

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
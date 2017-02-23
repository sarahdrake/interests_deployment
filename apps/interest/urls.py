from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^people$', views.people),
    url(r'^process$', views.process),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]

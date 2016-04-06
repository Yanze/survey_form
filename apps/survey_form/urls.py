from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^show$', views.show, name="show"),
)

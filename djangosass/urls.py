from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from views import home

urlpatterns = patterns('',
    url("^$", home, name="home"),
)

urlpatterns += staticfiles_urlpatterns()

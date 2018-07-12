#from django.conf.urls import include, url
from django.conf.urls import patterns, include, url
from django.contrib import admin
from jazz import views

urlpatterns = patterns('',
    url(r'^$', 'jazz.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls))
   )

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.views.static import serve
from django.conf.urls import url


app_name = 'video'
urlpatterns = [
    #listView
    path('', views.index, name = "index"),
    path('liat/', views.liat, name = "liat"),
    

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
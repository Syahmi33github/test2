from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . models import PostModels
from . import views

from django.views.generic import ListView

app_name = 'blog'
urlpatterns = [
    #listView
    path('page/<str:page>/', views.BlogListView.as_view(model=PostModels),  name = "listpage"),
    # path('category/<str:categoryInput>/', views.categoryPost.as_view(model=PostModels),  name = "category"),

    path('category/<str:categoryInput>/', views.categoryPost, name="category"),
    path('test/', views.testparallax, name="test"),
    path('post/<str:slugInput>/', views.detailPost, name="detail"),
    path('ceritasingkat/<str:slugInput>/', views.ceritaSingkat, name="ceritasingkat"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
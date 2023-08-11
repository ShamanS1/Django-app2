from django.urls import path

from . import views
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

urlpatterns = [
    path('', views.index, name='index'),
    
    
]
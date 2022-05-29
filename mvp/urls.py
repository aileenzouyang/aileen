from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('load', views.table, name='load'),
    #path('load', views.test, name='load'),
    path('remove', views.remove, name='remove'),
    path('removecolumns', views.removecolumns, name='removecolumns')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
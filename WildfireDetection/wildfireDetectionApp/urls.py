"""
    File to map urls to page views users will have
    For this project we will have the user registration page
    and the home page with the map
"""
from django.urls import path
from django.conf.urls import url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.cache import never_cache

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_registration/', views.user_registration, name='registration'),
    path('confirmation/', views.confirmation, name='confirmation'),
    url(r'ajax/markers/', never_cache(views.markers), name='markers')
] + staticfiles_urlpatterns()

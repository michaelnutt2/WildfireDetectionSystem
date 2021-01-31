"""
    File to map urls to page views users will have
    For this project we will have the user registration page
    and the home page with the map
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_registration/', views.user_registration, name='registration'),
    path('confirmation/', views.confirmation, name='confirmation')
]

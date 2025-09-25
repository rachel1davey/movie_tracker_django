from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_bar, name='search_bar'),
    path('profile/', views.own_profile, name='own_profile'),
    path('profile/<str:username>', views.user_profile, name='user_profile'),
]

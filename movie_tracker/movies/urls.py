from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/', views.movie_detail, name="movie_detail")
]

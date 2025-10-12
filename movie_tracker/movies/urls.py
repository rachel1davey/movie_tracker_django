from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

app_name = "movies"

urlpatterns = [
    path('<int:movie_id>/', views.movie_detail, name="movie_detail"),
    path('review/<int:review_id>/edit/', views.edit_review, name="edit_review"),
    path('review/<int:review_id>/delete/', views.delete_review, name="delete_review")
]

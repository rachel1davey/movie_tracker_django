from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_bar, name='search_bar'),
    path('profile/', views.own_profile, name='own_profile'),
    path('profile/edit/', views.edit_profile, name="edit_profile"),  # move before user_profile
    path('profile/settings/', views.profile_settings, name='profile_settings'),
    path('profile/delete/', views.delete_account, name='delete_account'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('profile/watchlist/toggle/<int:pk>/', views.toggle_watchlist_visibility, name='toggle_watchlist'),
    path('profile/watchlist/remove/<int:pk>/', views.remove_from_watchlist, name='remove_from_watchlist'),
]

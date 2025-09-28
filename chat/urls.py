from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room, name='chat_room'),
    path('fetch/', views.fetch_messages, name='fetch_messages'),
    path('send/', views.send_message, name='send_message'),
]

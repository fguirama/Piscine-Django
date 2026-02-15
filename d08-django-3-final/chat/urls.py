from django.urls import path

from chat.views import chats_view

urlpatterns = [
    path('', chats_view)
]

from django.urls import path

from chat.views import chat_view, chats_view

urlpatterns = [
    path('', chats_view, name='chat'),
    path('<int:chat_id>/', chat_view, name='chats')
]

from django.urls import path

from chat.views import chatrooms_view, chats_view

urlpatterns = [
    path('', chats_view, name='chats'),
    path('<int:chatroom_id>/', chatrooms_view, name='chatroom')
]

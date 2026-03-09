from django.shortcuts import render, get_object_or_404

from chat.models import Chatroom


def chats_view(request):
    chatrooms = Chatroom.objects.all()
    return render(request, 'chats.html', context={'chatrooms': chatrooms})


def chatrooms_view(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
    return render(request, 'chatroom.html', context={'chatroom': chatroom})

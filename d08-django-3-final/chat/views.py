from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from chat.models import Chatroom


@login_required
def chats_view(request):
    chatrooms = Chatroom.objects.all()
    return render(request, 'chats.html', context={'chatrooms': chatrooms})


@login_required
def chatrooms_view(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
    return render(request, 'chatroom.html', context={'chatroom': chatroom})

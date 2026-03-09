from django.shortcuts import render, get_object_or_404

from chat.models import Chat


def chats_view(request):
    chats = Chat.objects.all()
    return render(request, 'chats.html', context={'chats': chats})


def chat_view(request, chat_id):
    chat = get_object_or_404(Chat, pk=chat_id)
    return render(request, 'chat.html', context={'chat': chat})

from django.shortcuts import render


def chats_view(request):
    return render(request, 'chats.html')

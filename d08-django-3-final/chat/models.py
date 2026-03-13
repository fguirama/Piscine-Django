from django.contrib.auth.models import User
from django.db import models


class Chatroom(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name="messages")
    username = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.chatroom}] {self.username}: {self.message}'



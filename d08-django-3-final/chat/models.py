from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

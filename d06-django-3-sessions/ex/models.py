from django.db import models


class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

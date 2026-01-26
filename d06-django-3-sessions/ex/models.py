from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    rep_point = models.IntegerField(default=0)

    def update_reputation(self):
        tips = self.tips.all()
        total = 0
        for tip in tips:
            total += tip.upvotes.count() * 5
            total -= tip.downvotes.count() * 2
        self.rep_point = total
        self.save()
        if self.rep_point >= 15:
            self.user_permissions.add('ex.can_downvote_tip')
        else:
            self.user_permissions.remove('ex.delete_tip')

        if self.rep_point >= 30:
            self.user_permissions.add('ex.delete_tip')
        else:
            self.user_permissions.remove('ex.delete_tip')


class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tips')
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvotes')
    downvotes = models.ManyToManyField(User, related_name='downvotes')

    def upvotes_count(self):
        return self.upvotes.count()

    def downvotes_count(self):
        return self.downvotes.count()

    class Meta:
        permissions = [
            ('can_downvote_tip', 'Can downvote tips'),
        ]

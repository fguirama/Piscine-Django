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

    def can_downvote(self, tip=None):
        if tip and tip.author == self:
            return True
        return self.reputation >= 15

    def can_delete_tip(self, tip=None):
        if tip and tip.author == self:
            return True
        return self.reputation >= 30


class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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

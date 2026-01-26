from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class User(AbstractUser):
    rep_point = models.IntegerField(default=0)

    def update_reputation(self):
        tips = self.tips.all()
        total = 0
        for tip in tips:
            total += tip.upvotes.exclude(id=self.id).count() * 5
            total -= tip.downvotes.exclude(id=self.id).count() * 2
        self.rep_point = total
        self.save()
        downvote_perm = Permission.objects.get(codename='downvote_tip', content_type__app_label='ex')
        if self.rep_point >= 15:
            self.user_permissions.add(downvote_perm)
        else:
            self.user_permissions.remove(downvote_perm)

        delete_perm = Permission.objects.get(codename='delete_tip', content_type__app_label='ex')
        if self.rep_point >= 30:
            self.user_permissions.add(delete_perm)
        else:
            self.user_permissions.remove(delete_perm)


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
            ('downvote_tip', 'Can downvote tips'),
        ]

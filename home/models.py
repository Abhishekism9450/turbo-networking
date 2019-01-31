from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('home:post-detail', kwargs={'pk': self.pk})


class Friend(models.Model):
    users= models.ManyToManyField(User)
    current_user= models.ForeignKey(User, related_name='owner',null=True,on_delete='CASCADE')

    @classmethod
    def make_friend(cls, current_user , new_friend):
        friend, created= cls.objects.get_or_create(
        current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user , new_friend):
        friend, created= cls.objects.get_or_create(
        current_user=current_user
        )
        friend.users.remove(current_user,new_friend)

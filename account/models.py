from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    # 用户id
    user = models.OneToOneField(User, related_name='user_profile',unique=True, on_delete=models.CASCADE)
    # 用户昵称
    nickname = models.CharField(max_length=20, unique=True)
    # 手机号
    phone = models.CharField(max_length=20, null=True)

    def __srt__(self):
        return 'user {}'.format(self.user.username)


# class UserInfo(models.Model):
#     user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
#     school = models.CharField(max_length=100, blank=True)
#     company = models.CharField(max_length=100, blank=True)
#     profession = models.CharField(max_length=100, blank=True)
#     address = models.CharField(max_length=100, blank=True)
#     aboutme = models.TextField(blank=True)

    # photo = models.ImageField(blank=True)

    # def __str__(self):
    #     return 'user {}'.format(self.user.username)

from django.contrib.auth.models import User
from django.db import models


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, verbose_name="Bio", default="")

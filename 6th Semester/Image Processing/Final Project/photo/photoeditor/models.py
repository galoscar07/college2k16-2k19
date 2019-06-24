from django.contrib.auth.models import User
from django.db import models


class UploadImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    img = models.ImageField(upload_to='images/')

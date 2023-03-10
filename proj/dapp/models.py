from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(default='Basic', max_length=30)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()


class UploadImageModel(models.Model):
    image = models.ImageField(upload_to='images/')

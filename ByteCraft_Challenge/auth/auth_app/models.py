from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class customuser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(customuser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

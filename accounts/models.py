from django.db import models

# Create your models here.


class UserProfile(models.Model):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

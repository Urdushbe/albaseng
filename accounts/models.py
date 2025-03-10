from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    telegram = models.CharField(max_length=500, blank=True, null=True, default="Not filled in!")

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

class Scholarship(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Hardship(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BasicNeedSupport(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


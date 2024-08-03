# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='admin_profile', null=True, blank=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    NUID = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    role_within_dash = models.CharField(max_length=50)
    edits_made = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)

    def deactivate(self):
        self.is_active = False
        self.deactivated_at = timezone.now()
        self.save()

    def reactivate(self):
        self.is_active = True
        self.deactivated_at = None
        self.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.NUID})"

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    NUID = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    year = models.CharField(max_length=50)
    is_dash_member = models.BooleanField(default=False)
    scholarships = models.ManyToManyField('DASH_pillars.Scholarship', blank=True)
    hardships = models.ManyToManyField('DASH_pillars.Hardship', blank=True)
    basic_need_supports = models.ManyToManyField('DASH_pillars.BasicNeedSupport', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


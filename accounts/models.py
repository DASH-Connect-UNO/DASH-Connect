from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import json

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    NUID = models.CharField(max_length=8, unique=True, primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'NUID'
    REQUIRED_FIELDS = ['email']

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


class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, db_column='nuid')
    role_within_DASH = models.CharField(max_length=50)
    edits_made = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.NUID})"


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, db_column='nuid')
    year = models.CharField(max_length=50)
    DASH_Member = models.BooleanField(default=False)
    scholarships = models.ManyToManyField('DASH_pillars.Scholarship', blank=True)
    hardships = models.ManyToManyField('DASH_pillars.Hardship', blank=True)
    basic_need_supports = models.ManyToManyField('DASH_pillars.BasicNeedSupport', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


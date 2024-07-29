from django.db import models

class Scholarship(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hardship(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BasicNeedSupport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

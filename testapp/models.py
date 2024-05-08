from django.db import models

# Create your models here.
class HydJob(models.Model):
    date = models.DateTimeField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    # phonenumber = models.CharField(max_length=40)

class BngJob(models.Model):
    date = models.DateTimeField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    # phonenumber = models.CharField(max_length=40)

class PunJob(models.Model):
    date = models.DateTimeField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    # phonenumber = models.CharField(max_length=40)
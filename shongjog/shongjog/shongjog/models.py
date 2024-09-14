# models.py
from django.db import models
from django.contrib.auth.models import User
from all_services.models import ServiceItem

class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , blank=True, null=True)  # Linked with Django's User model
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=8, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    occupation = models.CharField(max_length=100)
    area = models.CharField(max_length=100 , blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Infomation_Home(models.Model):
    gmail = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    open_hour = models.CharField(max_length=100)
    footer_description = models.TextField(blank=True, null=True)
    copyright = models.CharField(max_length=100)
    design = models.CharField(max_length=100)

    def __str__(self):
        return self.gmail
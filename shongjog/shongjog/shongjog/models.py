# models.py
from django.db import models
from django.contrib.auth.models import User
from all_services.models import ServiceItem
from all_services.models import Services

class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , blank=True, null=True)  # Linked with Django's User model
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=8, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    occupation = models.CharField(max_length=100)
    area = models.CharField(max_length=100 , blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.occupation


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
class Top_product(models.Model):
    product = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='top_product')
    icon = models.CharField(max_length= 500)

class For_home(models.Model):
    product = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='For_home')
    picture = models.ImageField(upload_to='for_pictures/', blank=True, null=True)
    
class Recently_view(models.Model):
    product = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='recently_view')
    picture = models.ImageField(upload_to='recently_view/', blank=True, null=True)
    
class Trending(models.Model):
    product = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='trending')
    picture = models.ImageField(upload_to='trending/', blank=True, null=True)
    
class Recommended(models.Model):
    product = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='recommended')
    picture = models.ImageField(upload_to='recommended/', blank=True, null=True)

class Review(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length = 20)
    description = models.TextField()
    picture = models.ImageField(upload_to='review/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name 
     
class order(models.Model):
    caption = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return self.caption
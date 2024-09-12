from django.db import models

# Create your models here.

class EXCLUDE_SERVICE(models.Model):
    ls = models.TextField()
    services = models.ForeignKey('ServiceItem', related_name='exclude_service', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ls
class INCLUDE_SERVICE(models.Model):
    ls = models.TextField()
    services = models.ForeignKey('ServiceItem', related_name='include_service', on_delete=models.CASCADE)
    
    def  __str__(self):
        return self.ls


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    services = models.ForeignKey('ServiceItem', related_name='faq', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question
    
class ServiceItem(models.Model):
    service_name = models.CharField(max_length=200)
    service_description = models.TextField(null= True , blank=True)
    services = models.ForeignKey('Services', related_name='service_items', on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name


class Services(models.Model):
    service_name = models.CharField(max_length=200)
    image_1 = models.ImageField(upload_to="image/", null=True, blank=True)
    image_2 = models.ImageField(upload_to="image/", null=True, blank=True)
    image_3 = models.ImageField(upload_to="image/", null=True, blank=True)

    def __str__(self):
        return self.service_name

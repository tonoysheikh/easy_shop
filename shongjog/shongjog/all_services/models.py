from django.db import models

# Create your models here.
class Services(models.Model):
    service_name = models.CharField(max_length= 200)
    image_1 = models.ImageField(upload_to = "image/" , null= True , blank=True)
    image_2 = models.ImageField(upload_to = "image/" , null= True , blank=True)
    image_3 = models.ImageField(upload_to = "image/" , null= True , blank=True)
    all_service = models.TextField()
    
    def __str__(self):
        return self.service_name
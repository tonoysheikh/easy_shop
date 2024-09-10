from django.db import models

# Create your models here.
class ServiceItem(models.Model):
    service_name = models.CharField(max_length=200)
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

from django.contrib import admin

# Register your models here.

from .models import Services
from .models import ServiceItem

admin.site.register(Services)
admin.site.register(ServiceItem)

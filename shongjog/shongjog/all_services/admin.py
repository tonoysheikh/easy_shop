from django.contrib import admin

# Register your models here.

from .models import Services
from .models import ServiceItem
from .models import FAQ

admin.site.register(Services)
admin.site.register(ServiceItem)
admin.site.register(FAQ)

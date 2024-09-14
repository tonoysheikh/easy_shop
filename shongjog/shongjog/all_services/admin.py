from django.contrib import admin

from .models import Services
from .models import ServiceItem
from .models import FAQ
from .models import INCLUDE_SERVICE
from .models import EXCLUDE_SERVICE

admin.site.register(Services)
admin.site.register(ServiceItem)
admin.site.register(FAQ)
admin.site.register(INCLUDE_SERVICE)
admin.site.register(EXCLUDE_SERVICE)

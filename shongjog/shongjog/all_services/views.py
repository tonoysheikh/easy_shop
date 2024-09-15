from django.shortcuts import render
from .models import Services
from .models import ServiceItem
from .models import FAQ
from .models import INCLUDE_SERVICE
from .models import EXCLUDE_SERVICE
from shongjog.models import Registration

def all_services(request):
    search = request.GET.get('text')
    if search:
        search_todo = Services.objects.prefetch_related('service_items').filter(service_name__icontains= search)
    else :
        search_todo = Services.objects.prefetch_related('service_items').all()
    context = {
        'search_todo': search_todo,
    }
    return render(request, "all_services.html", context)

def seba(request, pk):
    serviceitem = ServiceItem.objects.get(pk=pk)
    faqs = FAQ.objects.filter(services = serviceitem)  
    include_services = INCLUDE_SERVICE.objects.filter(services = serviceitem)  
    exclude_services = EXCLUDE_SERVICE.objects.filter(services = serviceitem) 
    registrations = Registration.objects.all()

    context = {
        'serviceitem': serviceitem,
        'faqs': faqs,
        'include_ls': include_services,
        'exclude_ls': exclude_services,
        'registrations': registrations
    }
    return render(request, "seba.html", context)

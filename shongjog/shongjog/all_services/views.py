from django.shortcuts import render
from .models import Services
from .models import ServiceItem
from .models import FAQ

def all_services(request):
    
    search_todo = Services.objects.prefetch_related('service_items').all()
    context = {
        'search_todo': search_todo,
    }
    return render(request, "all_services.html", context)

def seba(request, pk):
    serviceitem = ServiceItem.objects.get(pk=pk)
    print(serviceitem)
    print(pk)
    faqs = FAQ.objects.filter(pk = pk) 
    context = {
        'serviceitem': serviceitem,
        'faqs': faqs
    }
    return render(request, "seba.html", context)

from django.shortcuts import render
from .models import Services

def all_services(request):
    search_todo = Services.objects.prefetch_related('service_items').all()
    context = {
        'search_todo': search_todo,
    }
    return render(request, "all_services.html", context)



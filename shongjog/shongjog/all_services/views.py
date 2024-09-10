from django.shortcuts import render
from django.http import HttpResponse
from .models import Services

def all_services(request):
    search_todo = Services.objects.all()
    context = {
        'search_todo': search_todo,
    }
    return render(request, "all_services.html" , context)

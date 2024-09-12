# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    

def profile(request):
    return render(request, 'profile.html')




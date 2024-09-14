from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from .models import Infomation_Home, Registration  # Add Registration model

def home(request):
    info_home = get_object_or_404(Infomation_Home)
    return render(request, "home.html", {"info_home": info_home})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Save the user instance
            return redirect('/login')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    

def profile(request):
    # Assuming you want to display the user's registration information
    registration = get_object_or_404(Registration, user=request.user)
    return render(request, 'profile.html', {'registration': registration})
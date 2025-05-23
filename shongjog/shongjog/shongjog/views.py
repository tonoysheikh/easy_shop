from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from .models import Infomation_Home, Registration  # Add Registration model
from django.contrib.auth import logout
from .forms import RegistrationForm, UpdateRegistrationForm
from django.contrib.auth.decorators import login_required 
from all_services.models import Services
from .models import Top_product
from .models import For_home
from .models import Recently_view
from .models import Trending
from .models import Review
from .models import Contact
from .models import Recommended
from .models import order


def home(request):
    info_home = get_object_or_404(Infomation_Home)
    search_todo = Services.objects.prefetch_related('service_items').all()
    top_products = Top_product.objects.all()
    for_home = For_home.objects.all()
    recently_view = Recently_view.objects.all()
    trending = Trending.objects.all()
    review = Review.objects.all()
    recommended = Recommended.objects.all()
    orders = order.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = Contact(name=name, email=email, subject = subject, message = message)
        contact.save()
        
    context = {
        'info_home': info_home,
        'search_todo' : search_todo,
        'top_products': top_products,
        'for_home' : for_home,
        'recently_view' : recently_view,
        'trending'  : trending,
        'review' : review,
        'recommended' : recommended,
        'orders' : orders,
    }
    return render(request, "home.html", context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Save the user instance
            return redirect('/login')
    else:
        form = RegistrationForm()
    info_home = get_object_or_404(Infomation_Home)
    search_todo = Services.objects.prefetch_related('service_items').all()
    
    context = {
        'form': form,
        'info_home': info_home,
        'search_todo' : search_todo,
    }
    return render(request, 'register.html', context)


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info_home'] = get_object_or_404(Infomation_Home)
        context['search_todo'] = Services.objects.prefetch_related('service_items').all()
        return context

    
    

def profile(request):
    registration = get_object_or_404(Registration, user=request.user)
    info_home = get_object_or_404(Infomation_Home)
    search_todo = Services.objects.prefetch_related('service_items').all()

    context = {
        'registration': registration,
        'info_home': info_home,
        'search_todo' : search_todo,
    }
    return render(request, 'profile.html', context)

@login_required 
def logout_view(request):
    logout(request)
    next_page = request.GET.get('next', '/')
    return redirect(next_page)
    

def update_profile(request):
    if request.method == 'POST':
        form = UpdateRegistrationForm(request.POST, request.FILES, instance=request.user.registration)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = UpdateRegistrationForm(instance=request.user.registration)
    
    
    info_home = get_object_or_404(Infomation_Home)
    search_todo = Services.objects.prefetch_related('service_items').all()
    context = {
        'info_home': info_home,
        'form': form,
        'search_todo' :search_todo,
    }
    
    return render(request, 'update_profile.html', context)

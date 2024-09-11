from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('' , views.all_services),
    path('<int:pk>/' , views.seba , name='seba'),
]


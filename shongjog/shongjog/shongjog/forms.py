# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Registration
from django.forms import ModelChoiceField
from all_services.models import ServiceItem

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)
    status = forms.ChoiceField(choices=[('active', 'Active'), ('inactive', 'Inactive')])
    occupation = ModelChoiceField(queryset=ServiceItem.objects.all(), required=True)
    area = forms.CharField(max_length = 100)
    picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number', 'status', 'occupation', 'picture' , 'area']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()

        registration = Registration(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            status=self.cleaned_data['status'],
            occupation=self.cleaned_data['occupation'],
            area =self.cleaned_data['area'],
            picture=self.cleaned_data.get('picture')
        )
        registration.save()
        return user

class UpdateRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['phone_number', 'status',  'area', 'picture' ]

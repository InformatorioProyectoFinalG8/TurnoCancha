from .models import Reserva
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        usuario='username'
        fields = ('dia', 'horario', 'cancha')
        #forms.fields['usuario'].widget = forms.HiddenInput()

        widgets={
            "dia": forms.SelectDateWidget()
        }

 

class NewUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class CustomUserCreationForm(UserCreationForm):
    
     
     class Meta:
         model = User
         fields = ["username", "first_name", "last_name", "email", "password1", "password2"]



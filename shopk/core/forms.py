from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms, widgets

class regi(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
               }

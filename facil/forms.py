from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ArticuloForm(forms.Form):
    nombre   = forms.CharField(max_length=67, required=True)
    modelo   = forms.CharField(max_length=40, required=True)


class RegistroForm(UserCreationForm):
    email   = forms.EmailField(max_length=67, required=True)
    password1  = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2   = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username','email','password1','password2']    
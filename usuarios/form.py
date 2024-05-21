from django.contrib.auth.models import User
from django import forms

class FormLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        label = {'username':'Login', 'password':'Senha'}
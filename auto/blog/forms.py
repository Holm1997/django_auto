from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddCarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brd'].empty_label = 'Не выбрано'
        self.fields['btype'].empty_label = 'Не выбрано'
        self.fields['carcl'].empty_label = 'Не выбрано'

    class Meta:
        model = Car
        fields = ['brd', 'title', 'birthday', 'photo', 'btype', 'carcl', 'description']
        
        
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }
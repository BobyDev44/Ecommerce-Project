from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class CrearUser(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            "username", 
            "email",
            "password1",
            "password2",
            ]
        # widgets = {
        #     "first_name": forms.TextInput(attrs={
        #         "class":"nombre"
        #     }),
        # }

        
class CrearSuperUser(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            "username", 
            "email",
            "password1",
            "password2",
            ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = True
        user.is_staff = True
        if commit:
            user.save()
        return user
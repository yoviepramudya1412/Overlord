from django import forms
from . models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            # Periksa kecocokan username dan password dengan model Admin
            admin = Admin.objects.filter(username=username).first()
            if admin is None or not admin.check_password(password):
                raise forms.ValidationError('Username atau password salah')
        
        return cleaned_data
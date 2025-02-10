from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    # Additional fields for Django user class
    email = forms.EmailField()
    birthday = forms.DateField()
    sex = forms.CharField(max_length=1)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    nationality = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'nationality', 'birthday', 'sex']
        widgets = {
            'birthday': forms.DateInput(attrs={'type':'date'})
        }
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    birthday = forms.DateField()
    sex = forms.CharField(max_length=1)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    nationality = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'nationality', 'birthday', 'sex']
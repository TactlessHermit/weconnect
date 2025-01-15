from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


# Create your views here.
def homepage(request):
    return render(request, "users/webpages/home.html")

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            #Save user details
            form.save()

            #Log in user and redirect to 'My Page'
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            user = authenticate(request, username=email, password=password)
            login(request, user)
            messages.success(request, "Registered successfully. Welcome.")
            return redirect(reverse('user:profile'))

    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration/register_user.html', {'form': form})

def login_user(request):

    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse('user:profile'))
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Log in failed. Check credentials.")
            return redirect(reverse('user:login'))

    else:
        return render(request, "users/registration/login.html")

def user_details(request):
    return render(request, "users/webpages/profile.html")

def logout_view(request):
    logout(request)
    # Redirect to a success page
    return redirect(reverse('user:home'))
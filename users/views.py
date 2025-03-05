import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


logger = logging.getLogger(__name__)

# Create your views here.
def homepage(request):
    """
    Description: 
    Renders homepage

    Parameters:
    request
    """

    logger.info("Redirecting to homepage")

    return render(request, "users/webpages/home.html")

def register_user(request):
    """
    Description: 
    Register new user. Redirects them to their profile page

    Parameters:
    request
    """
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        # If valid, save user details
        logger.info("CHECK:: Validating registration form data")
        if form.is_valid(): 
            logger.info("INFO:: Registration data valid.")
            new_user = form.save(commit=False)
            logger.info("INFO:: Setting email as username.")
            new_user.username = form.cleaned_data['email']
            new_user.set_password(form.cleaned_data['password2'])

            # If username is not the same as email ask for new input
            if new_user.username != form.cleaned_data['email']:
                form = UserRegistrationForm()
                # logger.warning("ISSUE:: Username must be the same as the email. Redirecting to registration page")
                # messages.info(request, "Username must be the same as the email.")
                return render(request, 'users/registration/register_user.html', {'form': form})

            new_user.save()
            logger.info("INFO:: Check successful. New user created and saved.")

            # Log in user and redirect to 'My Page'
            logger.info("INFO:: Attempting to log in New user.")
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                logger.info("INFO:: New user logged in successfully. Redirecting to profile page")
                messages.success(request, "Registered successfully. Welcome.")
                return redirect(reverse('user:profile'))
            else:
                logger.error("ERROR:: User saved but authentication failed. Unable to log in.")
                return HttpResponse('<h1> ERROR AUTHENTICATING USER!!! </h1><br><p>Password: %s</p>' %password)    
        else:
            logger.error("ERROR:: Registration data invalid.")
    # Request for webpage
    else:
        form = UserRegistrationForm()

    logger.info("INFO:: Loading registration page.")
    return render(request, 'users/registration/register_user.html', {'form': form})

def login_user(request):
    """
    Description: 
    Validate login credentials and log-in user

    Parameters:
    request
    """

    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        logger.info("INFO:: Authenticating login details.")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            logger.info("INFO:: Authentication successful. Attempting login.")
            login(request, user)
            logger.info("INFO:: Login successful. Redirecting to profile page.")
            # Redirect to a success page.
            return redirect(reverse('user:profile'))
        else:
            # Return an 'invalid login' error message.
            logger.error("ERROR: User authentication failed. Returning to login page.")
            messages.success(request, "User authentication failed. Check credentials.")
            return redirect(reverse('user:login'))

    else:
        logger.info("INFO:: Loading login page.")
        return render(request, "users/registration/login.html")

def user_details(request):
    """
    Description: 
    Renders current user's profile page

    Parameters:
    request
    """

    return render(request, "users/webpages/profile.html")

def logout_view(request):
    """
    Description: 
    Log out current user

    Parameters:
    request
    """
    logger.info("INFO:: Logging out user.")
    logout(request)
    # Redirect to a success page
    return redirect(reverse('user:home'))
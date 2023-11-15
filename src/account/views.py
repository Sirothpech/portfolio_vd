from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from utilisateur.forms import UserLoginForm, UserRegistrationForm
from utilisateur.models import UserProfile
from django.contrib import messages

def index(request):
    return render(request, "registration/index.html")

def register_user(request):
    """
    Handles user registration.

    This function takes a request object as input and returns a rendered HTML page with a registration form.
    If the request method is POST, the function validates the form data and creates a new user profile if the form is valid.
    If the passwords entered by the user match, the function saves the user and creates a corresponding user profile.
    The user is then logged in and redirected to their profile page.
    If there is an integrity error (e.g., duplicate username), an error message is displayed.
    If the request method is not POST, the function simply renders the registration form.

    Args:
        request (object): The HTTP request object containing information about the user's request.

    Returns:
        object: Rendered HTML page with the registration form.
    """

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    user = form.save()

                    UserProfile.objects.create(user=user)

                    login(request, user)
                    return redirect('profile')
                except IntegrityError:
                    messages.error(request, 'Ce nom d\'utilisateur existe déjà.')
            else:
                messages.error(request, 'Les mots de passe ne correspondent pas.')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def login_user(request):
    """
    Handles the login functionality for a user in a Django web application.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: If the form is valid and the user is logged in successfully, the function redirects the user to the 'profile' page.
        Otherwise, the function renders the 'registration/login.html' template with the form as a context variable.
    """
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_user(request):
    """
    Logs out a user if the request method is POST.

    Args:
        request (object): The HTTP request object containing information about the current request.

    Returns:
        object: A rendered HTML template named 'registration/deconnexion.html'.

    Example Usage:
        # Import necessary modules

        # Define the logout_user function
        @login_required
        def logout_user(request):
            if request.method == 'POST':
                logout(request)
            return render(request, 'registration/deconnexion.html')
    """
    if request.method == 'POST':
        logout(request)
    return render(request, 'registration/deconnexion.html')

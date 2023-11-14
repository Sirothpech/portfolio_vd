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
    if request.method == 'POST':
        logout(request)
    return render(request, 'registration/deconnexion.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser,UserProfile
from .forms import UserProfileForm
@login_required
def manage_users(request):
    users = CustomUser.objects.all()
    return render(request, 'manage_users.html', {'users': users})

@login_required
def deactivate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = False
    user.save()
    return redirect('manage_users')

@login_required
def activate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = True
    user.save()
    return redirect('manage_users')

@login_required
def profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = None

    return render(request, 'registration/profile.html', {'user_profile': user_profile})


@login_required
def create_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        # Si le formulaire de modification de profil est soumis
        if 'profile_form' in request.POST:
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('profile')

        # Si le formulaire de changement de mot de passe est soumis
        elif 'password_form' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                # Met à jour la session de l'utilisateur pour éviter une déconnexion involontaire
                update_session_auth_hash(request, user)
                return redirect('profile')

    else:
        form = UserProfileForm(instance=user_profile)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'registration/create_profile.html', {'form': form, 'password_form': password_form})

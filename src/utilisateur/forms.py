from django import forms
from .models import CustomUser, UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    """
    A form for user registration, specifically for the CustomUser model.

    Inherits from the UserCreationForm class provided by Django.

    Fields:
    - username: A CharField representing the username field in the form.
                It has a label "Nom d'utilisateur" and is rendered as a text input field
                with the CSS class "form-register" and a placeholder "Nom d'utilisateur".
    - password1: A CharField representing the password field in the form.
                It has a label "Mot de passe" and is rendered as a password input field
                with the CSS class "form-register" and a placeholder "Mot de passe".
    - password2: A CharField representing the password confirmation field in the form.
                It has a label "Confirmation du mot de passe" and is rendered as a password input field
                with the CSS class "form-register" and a placeholder "Confirmation du mot de passe".
    """

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-register', 'placeholder': 'Nom d\'utilisateur'}),
    )

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-register', 'placeholder': 'Mot de passe'})
    )

    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-register', 'placeholder': 'Confirmation du mot de passe'})
    )


class UserLoginForm(AuthenticationForm):
    """
    A form for user login and authentication.

    Inherits from the AuthenticationForm class provided by Django.
    Includes fields for username and password, with corresponding labels and input widgets.

    Example Usage:
    form = UserLoginForm(request.POST)
    if form.is_valid():
        # Perform login logic
    """

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'})
    )

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )


class UserProfileForm(forms.ModelForm):
    """
    A Django form for creating and updating user profiles.

    Fields:
    - first_name: A field for the user's first name.
    - last_name: A field for the user's last name.
    - date_of_birth: A field for the user's date of birth.
    - profile_picture: A field for the user's profile picture.
    - email: A field for the user's email address.
    - phone_number: A field for the user's phone number.
    - address: A field for the user's address.
    - postal_code: A field for the user's postal code.
    """

    class Meta:
        """
        Metadata for the UserProfileForm.

        - model: The model to be used (UserProfile).
        - fields: The fields to be included in the form.
        """
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'profile_picture','email', 'phone_number', 'address', 'postal_code']


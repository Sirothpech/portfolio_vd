from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    CustomUser class is a subclass of AbstractUser from Django's built-in authentication system.
    It extends the functionality of the base class by adding a get_full_name method.

    Example Usage:
    user = CustomUser.objects.create(username='john', email='john@example.com')
    user.first_name = 'John'
    user.last_name = 'Doe'
    user.save()

    full_name = user.get_full_name()
    print(full_name)  # Output: John Doe
    """

    def get_full_name(self):
        """
        Returns the full name of the user by concatenating the first_name and last_name fields.

        Returns:
        str: The full name of the user.
        """
        return f"{self.first_name} {self.last_name}"

class UserProfile(models.Model):
    """
    A Django model representing a user profile.

    Fields:
    - user: A one-to-one relationship field with the CustomUser model.
    - first_name: A character field to store the user's first name.
    - last_name: A character field to store the user's last name.
    - email: An email field to store the user's email address.
    - date_of_birth: A date field to store the user's date of birth.
    - profile_picture: An image field to store the user's profile picture. It is uploaded to the 'profile_pics/' directory and has a default image if not provided.
    - phone_number: A character field to store the user's phone number.
    - address: A character field to store the user's address.
    - postal_code: A character field to store the user's postal code.
    """

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/image_preview.jpg' )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=5, blank=True, null=True)

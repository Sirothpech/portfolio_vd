from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    date_joined = models.DateTimeField(auto_now_add=True)
    navbar_choice = models.CharField(max_length=20, null=True, blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

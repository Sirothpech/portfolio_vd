from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):



    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/image_preview.jpg' )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

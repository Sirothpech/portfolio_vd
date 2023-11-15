from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    """
    Represents a contact message.

    Fields:
    - nom: The name of the contact (max length: 255 characters).
    - email: The email of the contact.
    - message: The message of the contact.

    Methods:
    - __str__: Returns the name of the contact as a string.
    """

    nom = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=255, null=True)


    def __str__(self):
        """
        Returns the name of the contact as a string.
        """
        return self.nom

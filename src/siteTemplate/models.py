from django.db import models

from utilisateur.models import CustomUser


class SiteTemplate(models.Model):
    """
    Represents a site template.

    Fields:
    - name (CharField): The name of the template (max length: 100 characters).
    - description (TextField): The description of the template.
    - html_content (TextField): The HTML content of the template (default: '').
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    html_content = models.TextField(default='')

    def __str__(self):
        """
        Returns a string representation of the template by returning its name.
        """
        return self.name

class UserTemplate(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    template = models.ForeignKey(SiteTemplate, on_delete=models.CASCADE, default='')
    html_content = models.TextField(default='')

    def save(self, *args, **kwargs):
        # Personnalisez la logique de sauvegarde ici si nécessaire
        super().save(*args, **kwargs)

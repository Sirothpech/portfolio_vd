from django.db import models

from utilisateur.models import CustomUser


class SiteTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    html_content = models.TextField(default='')

    def __str__(self):
        return self.name

class UserTemplate(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    template = models.ForeignKey(SiteTemplate, on_delete=models.CASCADE, default='')
    html_content = models.TextField(default='')

    def save(self, *args, **kwargs):
        # Personnalisez la logique de sauvegarde ici si nécessaire
        super().save(*args, **kwargs)

# Generated by Django 4.2.4 on 2023-11-14 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0021_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]

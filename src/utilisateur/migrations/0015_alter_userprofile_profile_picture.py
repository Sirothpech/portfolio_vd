# Generated by Django 4.2.4 on 2023-11-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0014_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='profile_pics/default_image.jpeg', upload_to='profile_pics/'),
        ),
    ]
# Generated by Django 5.1 on 2024-08-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_remove_userprofile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
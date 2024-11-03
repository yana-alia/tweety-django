# Generated by Django 5.1.2 on 2024-11-01 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('name', models.CharField(blank=True, max_length=90, null=True)),
                ('bio', models.TextField(blank=True, max_length=255, null=True)),
                ('avatar', models.ImageField(blank=True, default='uploads/avatars/default.jpg', upload_to='uploads/avatars')),
                ('header', models.ImageField(blank=True, default='uploads/headers/default.jpg', upload_to='uploads/headers')),
            ],
        ),
    ]
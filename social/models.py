from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', 
                                related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=90, blank=True, null=True)
    bio = models.TextField(max_length=255, blank=True, null= True)
    avatar = models.ImageField(upload_to='uploads/avatars', default='uploads/avatars/default.jpg', blank=True)
    header = models.ImageField(upload_to='uploads/headers', default='uploads/headers/default.jpg', blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
    following = models.ManyToManyField(User, blank=True, related_name="following")
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
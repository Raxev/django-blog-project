from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
When a User is saved the post_save signal is sent. 
This signal is received by the receiver, which is the create_profile function, 
which takes all of the arguments that the post_save signal passed to it. 
One of those arguments is the instance of the User, and another argument is created. 
If that user was created, create a Profile object with the user = instance of the User that was created. 
"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

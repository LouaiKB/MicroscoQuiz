#this file is created for the signals, for each new user creat a new Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from .models import Profile 

#when a user is saved then send this signal which be revieved by this
#receiver, this receiver is this creat_profile function  
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, unique=True, default=None)
    total_score = models.IntegerField(default=0)
    component_score = models.IntegerField(default=0)
    microscopy_score = models.IntegerField(default=0)
    level = models.CharField(max_length=100, default="beginner")

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def get_total_score(self):
        self.total_score = self.component_score + self.microscopy_score
        self.update(self.total_score)
    
    def get_component_score(self):
        return self.component_score
    
    def get_microscopy_score(self):
        return self.microscopy_score
    
    def __str__(self) -> str:
        return self.user.username

    
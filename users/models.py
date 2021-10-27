from django.db import models
from django.contrib.auth.models import User
from biologicalquizapp.models import Question

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, unique=True, default=None)
    total_score = models.IntegerField(default=0)
    component_score = models.IntegerField(default=0)
    microscopy_score = models.IntegerField(default=0)
    level = models.CharField(max_length=100, default="beginner")

    def get_total_score(self):
        return self.total_score
    
    def get_component_score(self):
        return self.component_score
    
    def get_microscopy_score(self):
        return self.microscopy_score

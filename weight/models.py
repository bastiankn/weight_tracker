from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    weight = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    tbw = models.FloatField('Total Body Water', null=True, blank=True)
    bmi = models.FloatField('Body Mass Index', null=True, blank=True)
    muscle_mass = models.FloatField(null=True, blank=True)
    bone_density = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
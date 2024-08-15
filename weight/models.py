from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Mass(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,  
        related_name='mass'  
    )
    weight = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    tbw = models.FloatField('Total Body Water', null=True, blank=True)
    bmi = models.FloatField('Body Mass Index', null=True, blank=True)
    muscle_mass = models.FloatField(null=True, blank=True)
    bone_density = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
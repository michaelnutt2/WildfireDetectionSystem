from django.db import models
from django.forms import ModelForm

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=100)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=5)


class FireTracker(models.Model):
    camera_id = models.IntegerField(primary_key=False)
    fire_detected = models.BooleanField(default=False)
    live_feed = models.CharField(max_length=300)

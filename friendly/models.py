from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender_identity = models.CharField(max_length=100)
    languages = ArrayField(models.CharField(max_length=100))
    personal_description = models.TextField(null=True, blank=True)
    identities = ArrayField(models.CharField(max_length=100, null=True, blank=True), size=5, null=True, blank=True)
    interests = ArrayField(models.CharField(max_length=100, null=True, blank=True), size=10, null=True, blank=True)
    religions = ArrayField(models.CharField(max_length=100, null=True, blank=True), size=3, null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True, default='blank-profile-picture.png')

    def __str__(self):
        return self.user.username
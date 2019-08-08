from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender_identity = models.CharField(max_length=100)
    languages = ArrayField(models.CharField(max_length=100))
    zip_code = models.PositiveIntegerField(max_length=5)
    personal_description = models.TextField(null=True, blank=True)
    identities = ArrayField(models.CharField(max_length=100, null=True, blank=True), size=5, null=True, blank=True)
    interests = ArrayField(models.CharField(max_length=100, null=True, blank=True), size=10, null=True, blank=True)
    religions = ArrayField(models.CharField(max_length=100, null=True, blank=True), size=3, null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True, default='blank-profile-picture.png')

    def __str__(self):
        return self.user.username

class Match(models.Model):
    user_1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='primary_matches')
    user_2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='secondary_matches')
    validate = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_1.user.username} and {self.user_2.user.username}'

class Message(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='messages')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='messages')
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.author.user.username}, {self.match}, {self.time_stamp}'
from django.contrib import admin
from .models import Profile, Match, Message

# Register your models here.

admin.site.register(Profile)
admin.site.register(Match)
admin.site.register(Message)
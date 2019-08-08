from django import forms
from .models import Profile, Match, Message

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'gender_identity', 'languages', 'zip_code', 'identities', 'interests', 'religions', 'profile_image','personal_description')
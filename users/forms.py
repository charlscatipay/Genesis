from django import forms
from .models import UserProfile, UserCredential

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'firstname', 'lastname', 'email',
            'location',
        )

class UserCredentialForm(forms.ModelForm):
    class Meta:
        model = UserCredential
        fields = (
            'username', 'password',
        )

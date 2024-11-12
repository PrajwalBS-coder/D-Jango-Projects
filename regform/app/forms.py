from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':""}


class Profile_form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']
from django import forms
from .models import *
class AllinOneForm(forms.ModelForm):
    class Meta:
        model=AllinOne
        fields='__all__'
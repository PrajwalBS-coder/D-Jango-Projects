from django import forms
from .models import *
class Sform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
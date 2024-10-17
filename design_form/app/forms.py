from django import forms
from app.models import *
class Name(forms.Form):
    na=forms.CharField(label='Name',max_length=100)
    health_tips=forms.CharField(label='Tips',max_length=100)

class PatientDetails(forms.ModelForm):
    # na=forms.CharField(label='Name',max_length=100)
    # blood_gorup=forms.CharField(label='Blood Group',max_length=100)
    # date=forms.DateField(label='Name')
    # health_tips=forms.CharField(label='Tips',max_length=100)
    class Meta:
        model=Patient
        fields=['name','blood_group']

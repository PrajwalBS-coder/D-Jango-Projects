from django import forms
from app.models import *
class Name(forms.Form):
    na=forms.CharField(label='Name',max_length=100)

class PatientDetails(forms.ModelForm):
    class meta:
        model=Patient
        fields=['name','blood_group','health_tips']

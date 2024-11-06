from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    reemail = forms.CharField(max_length=100, required=False,label='Reenter Email')
    class Meta:
        model=Student
        fields='__all__'
    def clean(self):
        print(str(self.cleaned_data))
        em=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if(em!=re):
            raise forms.ValidationError('Error')
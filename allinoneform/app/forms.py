from django import forms
from .models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url','email']

class AccessForm(forms.ModelForm):
    class Meta:
        model=Access
        fields=['author','date']
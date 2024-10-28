from django import forms
from .models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=webpage
        # fields=['topic_name','email']
        fields='__all__'

class AccessForm(forms.ModelForm):
    class Meta:
        model=access
        fields='__all__'
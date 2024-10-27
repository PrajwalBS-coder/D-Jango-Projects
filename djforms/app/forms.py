from django import forms
from .models import *
class StudentForm(forms.Form):
    sname=forms.CharField()
    id=forms.IntegerField()
    email=forms.EmailField()
    url=forms.URLField()
    address=forms.CharField(widget=forms.Textarea())
    password=forms.CharField(widget=forms.PasswordInput())

    gen1=forms.ChoiceField(choices=[('Male','male'),('Female','female')])
    # gen=forms.ChoiceField(choices=[('Male','male'),('Female','female')],widget=forms.RadioSelect)



    course1=forms.MultipleChoiceField(choices=[('PY','PYTHON'),('DJ','Django')])
    # course=forms.MultipleChoiceField(choices=[('PY','PYTHON'),('DJ','Django')],widget=forms.CheckboxSelectMultiple())

class TopicForm(forms.Form):
    tn=forms.CharField()
class webpageForm(forms.Form):
    tn=forms.ModelChoiceField(queryset=topic.objects.all())
    nm=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()

class AccessForm(forms.Form):
    name=forms.ModelChoiceField(queryset=webpage.objects.all())
    author=forms.CharField()
    date=forms.DateField()
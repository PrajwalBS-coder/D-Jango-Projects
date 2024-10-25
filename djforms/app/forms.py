from django import forms

class StudentForm(forms.Form):
    sname=forms.CharField()
    id=forms.IntegerField()
    email=forms.EmailField()
    url=forms.URLField()
    address=forms.CharField(widget=forms.Textarea())
    password=forms.CharField(widget=forms.PasswordInput())

    # gen=forms.ChoiceField(choices=[('Male','male'),('Female','female')])
    gen=forms.ChoiceField(choices=[('Male','male'),('Female','female')],widget=forms.RadioSelect)



    # course=forms.MultipleChoiceField(choices=[('PY','PYTHON'),('DJ','Django')])
    course=forms.MultipleChoiceField(choices=[('PY','PYTHON'),('DJ','Django')],widget=forms.CheckboxSelectMultiple())
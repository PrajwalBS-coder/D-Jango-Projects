from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.
from .forms import *
from django.core.mail import send_mail

def Registration(re):
    if re.method=='POST' and re.FILES:
        UO=UserForm(re.POST)
        PO=Profile_form(re.POST,re.FILES)
        if UO.is_valid() and PO.is_valid():
            MUO=UO.save(commit=False)
            pw=UO.cleaned_data['password']
            MUO.set_password(pw)
            MUO.save()

            MPO=PO.save(commit=False)
            MPO.user_name=MUO
            MPO.save()


               #sENDING emAIL
            send_mail(
                "Registration",
                "SuccessFull😎✌",
                'legendamin007@gmail.com',
                [MUO.email],
                fail_silently=False)
            return hr('Done')
        
        
     
        
        
        else:
            return hr('Not Done')
    return render(re,'Registration.html',{'uform':UserForm(),'pform':Profile_form()})
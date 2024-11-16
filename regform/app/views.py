from django.shortcuts import render
from django.http import HttpResponse as hr,HttpResponseRedirect
# Create your views here.
from .forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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
                'your@gmail.com',
                [MUO.email],
                fail_silently=False)
            return hr('Done')
        
        
     
        
        
        else:
            return hr('Not Done')
    return render(re,'Registration.html',{'uform':UserForm(),'pform':Profile_form()})


def HomePage(re):
    if re.session.get('username'):
        return render(re,'home.html',{'name':re.session.get('username')})
    return render(re,'home.html')


def UserLogin(re):
    if re.method=='POST':
        na=re.POST['usn']
        paswd=re.POST['passwdw']
        AUO=authenticate(username=na,password=paswd)
        if AUO:
            if AUO.is_active:
                login(re,AUO)
                re.session['username']=na
                return HttpResponseRedirect(reverse('home'))
            else:
                hr('Not An Active User')
        else:
            hr('Invalid Data')


    return render(re,'userlogin.html')


@login_required
def UserLogout(re):
    logout(re)
    return HttpResponseRedirect(reverse('home'))

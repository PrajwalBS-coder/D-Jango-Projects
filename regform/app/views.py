from django.shortcuts import render
from django.http import HttpResponse as hr,HttpResponseRedirect
# Create your views here.
from .forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def Registration(re):
    if re.method=='POST':
        if re.FILES:
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
        else:
            UO=UserForm(re.POST)
            PO=Profile_form(re.POST)
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


    return render(re,'userlogin2.html')


@login_required
def UserLogout(re):
    logout(re)
    return HttpResponseRedirect(reverse('home'))


def Start(re):
    return render(re,'main.html')

def About(re):
    return render(re,'aboutus.html')

@login_required
def UserProfile(re):
    name=re.session.get('username')
    UO=User.objects.get(username=name)
    PO=Profile.objects.get(user_name=UO)
    return render(re,'profile.html',{'user':UO,'profile':PO})


@login_required
def ChangePassword(re):
    if re.method=='POST':
        name=re.session.get('username')
        pw=re.POST['pwd']
        UO=User.objects.get(username=name)
        UO.set_password(pw)
        UO.save()
        

    return render(re,'change_password.html')


def ResetPassword(re):
    if re.method=='POST':
        name=re.POST['usn']
        pw=re.POST['pwd']
        UO=User.objects.filter(username=name)
        if UO:
            UO[0].set_password(pw)
            UO[0].save()
    return render(re,'resetpassword.html')


def Edit(re):
    if re.method=='POST':
        name=re.session.get('username')
        UO=User.objects.get(username=name)
        PO=Profile.objects.get(user_name=UO)

        UO.username=re.POST['usn']
        PO.address=re.POST['address']
        PO.profile_pic=re.FILES['img']
        UO.email=re.POST['email']
        
        UO.save()
        PO.save()
        logout(re)
        return HttpResponseRedirect(reverse('login'))
    name=re.session.get('username')
    UO=User.objects.get(username=name)
    PO=Profile.objects.get(user_name=UO)
    return render(re,'edit.html',{'user':UO,'profile':PO})
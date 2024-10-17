from django.shortcuts import render
from django.http import HttpResponse as hr
from django.http import HttpResponseRedirect as hred
from .forms import * 
# Create your views here.
def get_name(re):
    if re.method=="POST":
        form=Name(re.POST)
        if form.is_valid():
            # return hr("/OK Done/")
            return hred('/thank/')
            
    else:
        form=Name()
    return render(re,'na.html',{'form':form})

def thank(re):
    return render(re,'thanks.html')

def Patients_details(re):
    details=Patient.objects.all()
    if re.method=="POST":
        form=PatientDetails(re.POST)
        if 'delete' in re.POST:
            print("delete")
            pk=re.POST.get('delete')
            print(pk)
            Patient.objects.get(id=pk).delete()
        if form.is_valid():
            form.save()
            return hred('/thank/')
    else:
        form=PatientDetails()
        
    return render(re,'na.html',{'form':form,'details':details})
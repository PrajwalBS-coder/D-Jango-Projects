from django.shortcuts import render
from .forms import *
from django.http import HttpResponse as hr
# Create your views here.
def Insertall(re):
    if re.method=='POST':
        data=TopicForm(re.POST)
        if(data.is_valid()):
            data.save()

            #Above Code Save Topic data



            data2=WebpageForm(re.POST)
            if(data2.is_valid()):
                instance = data2.save(commit=False)
                to=Topic.objects.get(topic_name=data.cleaned_data['topic_name'])
                instance.topic_name = to  # Manually set the value here
                instance.save()


                     #Above Code Save Webpage's data

                data3=AccessForm(re.POST)
                if data3.is_valid():
                    instance = data3.save(commit=False)
                    wo=Webpage.objects.get(name=data2.cleaned_data['name'])
                    instance.name = wo  # Manually set the value here
                    instance.save()


                     #Above Code Save Access's data
                    
                else:
                    hr('Error In Acces')
            else:
                hr('Error In Webpage')
        else:
            hr('Error In Topic')

    return render(re,'allform.html',{'tform':TopicForm(),'wform':WebpageForm(),'aform':AccessForm()})
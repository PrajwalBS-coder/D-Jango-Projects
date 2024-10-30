from django.contrib import admin

# Register your models here.
from .models import *

class Custmizations_Webpage(admin.ModelAdmin):
    list_display=['topic_name','email','name']
    list_display_links=['email']
    list_editable=['name']
    # list_per_page=1
    list_filter=['name']
    search_fields=['name']

class Custmizations_Access(admin.ModelAdmin):
    list_display=['name','author']
    list_display_links=['author']
    list_editable=['name']
    # list_per_page=1
    list_filter=['name']
    search_fields=['name']



admin.site.register(topic)
admin.site.register(webpage,Custmizations_Webpage)
admin.site.register(access,Custmizations_Access)
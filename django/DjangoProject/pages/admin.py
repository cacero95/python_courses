from django.contrib import admin
from .models import Page # the . means this folder
# Register your models here.
admin.site.register(Page)
# Panel settings 
admin.site.site_header = 'Django projects'
admin.site.site_title = 'Management Panel'
admin.site.index_title = 'Management Panel'

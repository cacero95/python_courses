from django.contrib import admin
from .models import Word
# Register your models here.

admin.site.register(Word)

admin.site.site_header = "Learn words"
admin.site.site_title = "Learn words"

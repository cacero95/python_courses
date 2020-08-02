from django.contrib import admin
from .models import Article, Category

# Register your models here.

# for show the date fields in the admin
# the next class extends from the ModelAdmin
# and it can describe the read fields and the customizable fields
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# change the admin name and titles
admin.site.site_header = "Master in Python"
admin.site.site_title = "Master in Python"
admin.site.index_title = "Master in Panel"
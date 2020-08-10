from django.contrib import admin
from .models import Category, Article
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

    #Always when a element will save in the dba this method will display
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            # at the request.user goes the user logged
            # and the obj has all the properties models
            obj.user_id = request.user.id
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
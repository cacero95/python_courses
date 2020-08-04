from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    slug = models.CharField(max_length=150, verbose_name='Friendly field', unique=True)
    visible = models.BooleanField(verbose_name='Visible')
    craeted_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated at')
    
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(request):
        return self.title
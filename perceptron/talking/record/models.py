from django.db import models

# Create your models here.
class Word( models.Model ):
    content = models.TextField(verbose_name='Contenido')
    content_type = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"
        ordering = ['created_at']
    def __str__(self):
        return f"{self.content} - {self.content_type}"

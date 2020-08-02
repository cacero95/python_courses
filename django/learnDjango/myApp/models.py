from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(verbose_name = 'contenido') # traduce the variable name for django to spanish
    image = models.ImageField(default='null', verbose_name="Image", upload_to='articles')# let a field with a default value
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at") # set auto_now_add for let date vy default when the register was done
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Updated at")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        # ordering = ['public'] # order the table data first the public elements
        # ordering = ['id'] # order the table data by id asc
        # ordering = ['-id'] # order the table data by id desc
        ordering = ['created_at'] # order the table data by the publication date
    
    # with this method all the elements in the admin go to have a default text defined by the method
    def __str__(self):
        return f" {self.title} created at {self.created_at} {'Publicado' if self.public else 'No publicado'} "

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
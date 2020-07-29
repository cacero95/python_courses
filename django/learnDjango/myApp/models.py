from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='null')# let a field with a default value
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True) # set auto_now_add for let date vy default when the register was done
    updated_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
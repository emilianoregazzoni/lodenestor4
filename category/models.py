from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique= True)
    description = models.CharField(max_length=255, blank= True)
    slug = models.CharField(max_length=100, unique= True) # ecom, parte final de la url que representa la entidad
    cat_image = models.ImageField(upload_to = 'photos/categories', blank= True)

    class Meta: # para setear el nombre del admin de a entidad
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.category_name



from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    label = models.fields.CharField(max_length=100)
    active = models.BooleanField(default=True)

class Article(models.Model):
   title = models.CharField(max_length= 100)
   description = models.fields.CharField(max_length=1000)
   year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
   category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)


   

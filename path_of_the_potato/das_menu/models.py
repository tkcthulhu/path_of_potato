from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.FloatField()
    stock = models.BooleanField()
    spicy_level = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.title}'

# Create your models here.

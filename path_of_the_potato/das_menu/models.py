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
    description = models.CharField(max_length=200)
    price = models.FloatField()
    spicy_level = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.title}// Desc: {self.description}// Price: {self.price}// Spicyness: {self.spicy_level}// Category: {self.category}// Cuisine: {self.cuisine}'

# Create your models here.

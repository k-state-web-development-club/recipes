from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Recipe(model.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)

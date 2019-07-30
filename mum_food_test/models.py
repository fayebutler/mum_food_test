from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True)
    vegan = models.BooleanField()


class Recipe(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True)
    likes = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(Ingredient, related_name='+', blank=True)

    @property
    def vegan(self):
        for ingredient in self.ingredients.all():
            if not ingredient.vegan:
                return False
        return True


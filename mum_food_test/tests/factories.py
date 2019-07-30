import random

import factory

from mum_food_test import models


class IngredientFactory(factory.DjangoModelFactory):
    name = factory.Faker('word')
    vegan = random.choice([True, False])

    class Meta:
        model = models.Ingredient


class RecipeFactory(factory.DjangoModelFactory):
    name = factory.Faker('word')
    likes = factory.Faker('pyint')

    @factory.post_generation
    def ingredients(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of developers were passed in, use them
            for ingredient in extracted:
                self.ingredients.add(ingredient)

    class Meta:
        model = models.Recipe

from django.contrib import admin

from mum_food_test import models

admin.site.register(models.Ingredient)
admin.site.register(models.Recipe)

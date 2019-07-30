from rest_framework import viewsets

from mum_food_test import serializers, models


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IngredientSerializer
    queryset = models.Ingredient.objects.all()


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = models.Recipe.objects.all().order_by('')

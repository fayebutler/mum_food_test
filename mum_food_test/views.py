from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from mum_food_test import serializers, models


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IngredientSerializer
    queryset = models.Ingredient.objects.all()


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer

    def get_queryset(self):
        queryset = models.Recipe.objects.all().order_by('likes')

        ingredients = self.request.query_params.get('ingredients', None)
        vegan = self.request.query_params.get('vegan', None)

        if vegan:
            queryset = queryset.exclude(
                ingredients__vegan=False
            ).order_by('likes').distinct()

        if ingredients:
            ingredient_objs = [
                models.Ingredient.objects.get(name=ingredient)
                for ingredient in ingredients.split(',')
            ]
            queryset = queryset.filter(
                ingredients__in=ingredient_objs
            ).order_by('likes').distinct()

        return queryset

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):  # Parameters not used, but needed for rest framework else will error
        recipe = self.get_object()
        recipe.likes += 1
        recipe.save()
        data = self.get_serializer(recipe).data
        return Response(data)

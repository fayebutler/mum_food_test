from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from mum_food_test import serializers, models


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IngredientSerializer
    queryset = models.Ingredient.objects.all()


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = models.Recipe.objects.all().order_by('likes')

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):  # Parameters not used, but needed for rest framework else will error
        recipe = self.get_object()
        recipe.likes += 1
        recipe.save()
        data = self.get_serializer(recipe).data
        return Response(data)

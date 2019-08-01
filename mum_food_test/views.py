from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from mum_food_test import serializers, models, auth


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IngredientSerializer
    queryset = models.Ingredient.objects.all()
    lookup_field = 'name'


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer
    permission_classes = (auth.IsAuthenticatedOrReadLikeOnly,)
    lookup_field = 'name'

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

    def create(self, request, *args, **kwargs):
        ingredients = [
            models.Ingredient.objects.get(name=ingredient)
            for ingredient in request.data.get('ingredients', '').split(',')
        ]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        recipe = models.Recipe(**serializer.data)
        recipe.save()
        recipe.ingredients.add(*ingredients)
        recipe.save()
        serializer = self.get_serializer(recipe)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

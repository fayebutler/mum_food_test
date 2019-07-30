from rest_framework import serializers
from django.contrib.auth.models import User

from mum_food_test.models import Recipe, Ingredient


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'email', 'first_name', 'last_name', 'id'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = '__all__'

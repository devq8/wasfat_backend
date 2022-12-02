from rest_framework import serializers
from recipes.models import Category, Recipe, Ingredient, Quantity

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'category', 'title', 'prepTime', 'cookTime', 'servings', 'method', 'image',]

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image',]

from rest_framework import serializers
from recipes.models import Category, Recipe, Ingredient, Quantity

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image',]


class RecipeListSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer(); 

    class Meta:
        model = Recipe
        fields = ['id', 'category', 'title', 'prepTime', 'cookTime', 'servings', 'method', 'image',]

